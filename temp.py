import pandas as pd

# 1. 加载下载的大文件
# 确保路径正确
df = pd.read_csv('data/owid-co2-data.csv')

# 2. 筛选需要的列
cols = ['country', 'year', 'iso_code', 'co2_per_capita']
df_filtered = df[cols].copy()

# 3. 过滤年份：1990年以后的数据
df_filtered = df_filtered[df_filtered['year'] >= 1990]

# 4. ISO 代码转换为数字 ID 映射表
iso_to_id = {
    'AFG': 4, 'ALB': 8, 'DZA': 12, 'AGO': 24, 'ARG': 32, 'ARM': 51, 'AUS': 36, 'AUT': 40, 'AZE': 31,
    'BGD': 50, 'BLR': 112, 'BEL': 56, 'BLZ': 84, 'BEN': 204, 'BTN': 64, 'BOL': 68, 'BIH': 70, 'BWA': 72,
    'BRA': 76, 'BRN': 96, 'BGR': 100, 'BFA': 854, 'BDI': 108, 'KHM': 116, 'CMR': 120, 'CAN': 124, 'CHL': 152,
    'CHN': 156, 'COL': 170, 'COG': 178, 'CRI': 188, 'CIV': 384, 'HRV': 191, 'CUB': 192, 'CYP': 196, 'CZE': 203,
    'DNK': 208, 'DOM': 214, 'ECU': 218, 'EGY': 818, 'SLV': 222, 'EST': 233, 'ETH': 231, 'FJI': 242, 'FIN': 246,
    'FRA': 250, 'GAB': 266, 'GMB': 270, 'GEO': 268, 'DEU': 276, 'GHA': 288, 'GRC': 300, 'GTM': 320, 'GIN': 324,
    'GUY': 328, 'HTI': 332, 'HND': 340, 'HUN': 348, 'ISL': 352, 'IND': 356, 'IDN': 360, 'IRN': 364, 'IRQ': 368,
    'IRL': 372, 'ISR': 376, 'ITA': 380, 'JAM': 388, 'JPN': 392, 'JOR': 400, 'KAZ': 398, 'KEN': 404, 'KOR': 410,
    'KWT': 414, 'KGZ': 417, 'LAO': 418, 'LVA': 428, 'LBN': 422, 'LSO': 426, 'LBR': 430, 'LBY': 434, 'LTU': 440,
    'LUX': 442, 'MDG': 450, 'MWI': 454, 'MYS': 458, 'MLI': 466, 'MRT': 478, 'MEX': 484, 'MDA': 498, 'MNG': 496,
    'MAR': 504, 'MOZ': 508, 'MMR': 104, 'NAM': 516, 'NPL': 524, 'NLD': 528, 'NZL': 554, 'NIC': 558, 'NER': 562,
    'NGA': 566, 'NOR': 578, 'OMN': 512, 'PAK': 586, 'PAN': 591, 'PNG': 598, 'PRY': 600, 'PER': 604, 'PHL': 608,
    'POL': 616, 'PRT': 620, 'QAT': 634, 'ROU': 642, 'RUS': 643, 'RWA': 646, 'SAU': 682, 'SEN': 686, 'SRB': 688,
    'SLE': 694, 'SVK': 703, 'SVN': 705, 'SOM': 706, 'ZAF': 710, 'ESP': 724, 'LKA': 144, 'SDN': 729, 'SUR': 740,
    'SWZ': 748, 'SWE': 752, 'CHE': 756, 'SYR': 760, 'TWN': 158, 'TJK': 762, 'TZA': 834, 'THA': 764, 'TGO': 768,
    'TTO': 780, 'TUN': 788, 'TUR': 792, 'TKM': 795, 'UGA': 800, 'UKR': 804, 'ARE': 784, 'GBR': 826, 'USA': 840,
    'URY': 858, 'UZB': 860, 'VEN': 862, 'VNM': 704, 'ESH': 732, 'YEM': 887, 'ZMB': 894, 'ZWE': 716
}

# 5. 应用转换
df_filtered['id'] = df_filtered['iso_code'].map(iso_to_id)

# 6. 清洗数据
# 剔除 ID 为空的行
df_final = df_filtered.dropna(subset=['id']).copy()

# 【核心修改】：强制将 ID 转换为整数，去除 .0
df_final['id'] = df_final['id'].astype(int)

# 填充排放量的缺失值为 0（可选，也可选择 dropna）
df_final['co2_per_capita'] = df_final['co2_per_capita'].fillna(0)

# 7. 保存
df_final.to_csv('data/data_processed.csv', index=False)

print("处理完成！生成的 data_processed.csv 中 ID 已修正为整数格式。")