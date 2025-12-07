#!/usr/bin/env python3
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
print("Kaleido available:", pio.kaleido.scope is not None)

# CSV 読み込み
df = pd.read_csv("results.csv")

# program ごとに集計
summary = df.groupby("program")["time"].agg(["mean", "std"]).reset_index()

# 棒グラフ（エラーバー付き）
fig = go.Figure(
    data=[
        go.Bar(
            x=summary["program"],
            y=summary["mean"],
            error_y=dict(
                type="data",
                array=summary["std"],
                visible=True
            ),
            marker=dict(color="rgb(50,130,230)")
        )
    ]
)

fig.update_layout(
    title="Benchmark Results (mean ± std)",
    xaxis_title="Program",
    yaxis_title="Time (seconds)",
    template="plotly_dark",
    width=1000,
    height=600
)

# PNG 保存
try:
    fig.write_image("benchmark_results.png")
    print("Saved → benchmark_results.png")
except Exception as e:
    print("Error while saving image:", e)
