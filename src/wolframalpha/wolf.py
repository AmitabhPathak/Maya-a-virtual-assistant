import wolframalpha
def calculate(query):
    app_id="4UJQRT-7LJEWV7WT2"
    client=wolframalpha.Client(app_id)
    res=client.query(q)
    answer=next(res.results).text
    return answer
