from typing import List

from mcdreforged.api.utils.serializer import Serializable


class JrrpConfig(Serializable):
	online_mode: bool = True
	start: str = "你今天的人品值是："
	end: str = ""
	title: bool = False
	command: List[str] = ["!!jrrp"]
	message: List[dict] = [
		{
			"expr": "jrrp == 100",
			"start": "！！！！！你今天的人品值是：",
			"end": "！100！100！！！！！",
			"title": True
		},
		{
			"expr": "jrrp == 99",
			"end": "！但不是 100……"
		},
		{
			"expr": "jrrp >= 90",
			"end": "！好评如潮！"
		},
		{
			"expr": "jrrp >= 60",
			"end": "！是不错的一天呢！"
		},
		{
			"expr": "jrrp > 50",
			"end": "！还行啦还行啦。"
		},
		{
			"expr": "jrrp == 50",
			"end": "！五五开……"
		},
		{
			"expr": "jrrp >= 40",
			"end": "！还……还行吧……？"
		},
		{
			"expr": "jrrp >= 11",
			"end": "！呜哇……"
		},
		{
			"expr": "jrrp >= 1",
			"end": "……（没错，是百分制）",
		},
		{
			"expr": "True",
			"end": "……"
		}
	]
