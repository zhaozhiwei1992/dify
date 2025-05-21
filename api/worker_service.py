if __name__ == "__main__":
    # idea中配置
    # 1. 增加运行命令
    # /home/zhaozhiwei/workspace/dify/api/.venv/bin/celery
    # 2. 配置运行参数
    # -A app.celery worker -P gevent -c 1 --loglevel INFO -Q dataset,generation,mail,ops_trace,app_deletion

    # 最终在idea效果与官方直接执行效果一样，但是可以调试了
    #   uv run celery -A app.celery worker -P solo --without-gossip
    #   --without-mingle -Q dataset,generation,mail,ops_trace --loglevel INFO
    pass
