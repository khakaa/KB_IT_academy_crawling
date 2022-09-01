from flask import Flask

app = Flask(__name__) # 웹서버

@app.route("/")
def main():
    return '''
    <h1>Hello harin,Park!</h1>
    <a href="/next">Go Next</a>
    '''

@app.route("/next")
def next():
    return '''
    <h1>Next Page</h1>
    <a href="/">Go Home</a>
    '''

# 직접 실행시 __name__에 __main__이 저장된다.
if __name__ == "__main__":
    # host='0.0.0.0' -> 누구나 접속할 수 있도록 함. 설정 안해주면 본인만 접속 가능
    # debug True -> 코드 변경시 새로고침 역할
    app.run(host='0.0.0.0', port=8080, debug=True)