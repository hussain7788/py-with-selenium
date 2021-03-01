data = {"notif":[{"global_count":1,"type":"client","dtype":"Client Messages(s)","records":[{"id":1,"count":1,"name":"Percy Jackson","initialis":"PJ","msg":"hi this is client percy","time":"11 days ago","user_id":1}]},{"global_count":9,"type":"team","dtype":"Team Message(s)","records":[{"id":10,"count":1,"name":"0_client_9 last","initialis":"0L","msg":"Hi Team Msg","time":"11 days ago","user_id":10},{"id":9,"count":1,"name":"0_client_8 last","initialis":"0L","msg":"Hi Team Msg","time":"11 days ago","user_id":9},{"id":8,"count":1,"name":"0_client_7 last","initialis":"0L","msg":"Hi Team Msg","time":"11 days ago","user_id":8},{"id":7,"count":1,"name":"0_client_6 last","initialis":"0L","msg":"Hi Team Msg","time":"11 days ago","user_id":7},{"id":6,"count":1,"name":"0_client_5 last","initialis":"0L","msg":"Hi Team Msg","time":"11 days ago","user_id":6},{"id":4,"count":1,"name":"Hazel Levesque","initialis":"HL","msg":"Hi Team Msg","time":"11 days ago","user_id":4},{"id":3,"count":1,"name":"Frank Zhang","initialis":"FZ","msg":"Hi Team Msg","time":"11 days ago","user_id":3},{"id":2,"count":1,"name":"Annabeth Chase","initialis":"AC","msg":"Hi Team Msg","time":"11 days ago","user_id":2},{"id":1,"count":1,"name":"Percy Jackson","initialis":"PJ","msg":"Hi Team Msg","time":"11 days ago","user_id":1}]},{"global_count":10,"type":"todo","dtype":"Todo(s)","records":[{"id":1,"count":2,"time":"10 days ago","name":"Percy Jackson","initialis":"PJ","user_id":1},{"id":5,"count":4,"time":"10 days ago","name":"Leo Valdez","initialis":"LV","user_id":5},{"id":10,"count":3,"time":"11 days ago","name":"0_client_9 last","initialis":"0L","user_id":10},{"id":9,"count":3,"time":"11 days ago","name":"0_client_8 last","initialis":"0L","user_id":9},{"id":8,"count":3,"time":"11 days ago","name":"0_client_7 last","initialis":"0L","user_id":8},{"id":7,"count":3,"time":"11 days ago","name":"0_client_6 last","initialis":"0L","user_id":7},{"id":6,"count":3,"time":"11 days ago","name":"0_client_5 last","initialis":"0L","user_id":6},{"id":4,"count":3,"time":"11 days ago","name":"Hazel Levesque","initialis":"HL","user_id":4},{"id":3,"count":3,"time":"11 days ago","name":"Frank Zhang","initialis":"FZ","user_id":3},{"id":2,"count":3,"time":"11 days ago","name":"Annabeth Chase","initialis":"AC","user_id":2}]},{"global_count":1,"type":"internal_todo","dtype":"Auto Todo(s)","records":[{"id":5,"count":16,"time":"10 days ago","name":"Leo Valdez","initialis":"LV","user_id":5}]}]}

for i,y in data.items():
    a= 0
    count = 0
    while a != len(y):
        # print(y[a])
        for k,y in y[a].items():
            print("key is ", k)
            print("value is", y)
            
        a += 1
        count += 1
print("count is", count)
print("data is",data['notif'][0])
