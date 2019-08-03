from scrapy import cmdline

task_list = [
    # "LianJiaErShouFang",
    "LianJiaLouPan"
]

for task in task_list:
    cmd = f'scrapy crawl {task}'
    cmdline.execute(cmd.split())
