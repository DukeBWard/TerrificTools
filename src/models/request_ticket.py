class request_ticket:
    def __init__(self, reqid, date_needed, duration, status, userid, toolowner, return_date):
        self.reqid = reqid
        self.date_needed = date_needed
        self.duration = duration
        self.status = status
        self.userid = userid
        self.toolowner = toolowner
        self.return_date = return_date
