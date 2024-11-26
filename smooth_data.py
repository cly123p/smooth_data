import numpy as np
import matplotlib.pyplot as plt


def smooth_data(data, window_size):
    """对数据进行移动平均平滑"""
    return np.convolve(data, np.ones(window_size) / window_size, mode='valid')


def read_spectrum_data(file_path):
    frequencies = []
    amplitudes = []

    # 读取文件并解析数据
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            data = line.strip().split()
            if len(data) >= 2:  # 确保每行至少有两个数据
                freq = float(data[0])
                amp = float(data[1])
                frequencies.append(freq)
                amplitudes.append(amp)

    return np.array(frequencies), np.array(amplitudes)


def plot_spectrum(frequencies, amplitudes, smoothed_amplitudes):
    plt.figure(figsize=(10, 6))

    # 绘制原始幅度
    plt.plot(frequencies, amplitudes, label='Original amplitude', alpha=0.5)

    # 绘制平滑后的幅度
    plt.plot(frequencies[len(frequencies) - len(smoothed_amplitudes):], smoothed_amplitudes, label='Smoothed amplitude',
             color='orange')

    plt.title('Smoothed spectrum')
    plt.xlabel('f (Hz)')
    plt.ylabel('A')
    plt.legend()
    plt.grid(True)
    plt.show()


def main(file_path, window_size=5):
    frequencies, amplitudes = read_spectrum_data(file_path)

    # 对幅度进行平滑处理
    smoothed_amplitudes = smooth_data(amplitudes, window_size)

    # 绘制结果
    plot_spectrum(frequencies, amplitudes, smoothed_amplitudes)


# 调用函数并传入你的文件路径和窗口大小
main('data/30hz-f-1.txt', window_size=10)  # tip: 窗口大小越大，平滑效果越好
