

class TestEvents:

    def setup_class(self):
        pass

    def teardown_class(self):
        pass

    def test_getEvents(self):

        json = {

                "summary": "日程标题",
                "description": "日程描述",
                "need_notification": False,
                "start_time": {
                    "date": " 2018-09-01",
                    "timestamp": "1605024000",
                    "timezone": "Asia/Shanghai"
                },
                "end_time": {
                    "date": " 2018-09-01",
                    "timestamp": "1605024000",
                    "timezone": "Asia/Shanghai"
                },
                "vchat": {
                    "vc_type": "third_party",
                    "icon_type": "vc",
                    "description": "发起视频会议",
                    "meeting_url": "https://example.com"
                },
                "visibility": "default",
                "attendee_ability": "can_see_others",
                "free_busy_status": "busy",
                "location": {
                    "name": "地点名称",
                    "address": "地点地址",
                    "latitude": xxxxx,
                    "longitude": xxxxx
                },
                "color": -1,
                "reminders": [
                    {
                        "minutes": 5
                    }
                ],
                "recurrence": "FREQ=DAILY;INTERVAL=1",
                "schemas": [
                    {
                        "ui_name": "ForwardIcon",
                        "ui_status": "hide",
                        "app_link": "xxxxx"
                    }
                ]
            }
