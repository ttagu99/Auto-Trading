# %%
from backtesting import Backtest
from DwStrategy import DwStrategy_wRollover


from gather_data import load_feature_df
start_date = "2010-01-01"
end_date = "2023-05-30"
cold_start_num = 10
target_col = 'CL=F'
feature_df = load_feature_df(start_date, end_date, target_col)

# %%
# 백테스팅 조건
bt = Backtest(feature_df, DwStrategy_wRollover, cash=10000, commission=0.001)
results = bt.run()


# %%
# results 결과저장
print(results)
with open(f'../results/{target_col}_prediction.txt', 'w') as f:
    f.write(str(results))
result_fig = bt.plot(filename=f'../results/{target_col}_prediction.html')


# %%
