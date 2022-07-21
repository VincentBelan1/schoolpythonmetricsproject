from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"
serverPort = 9090


def metricsscrape():
    f = open('termdumbtoptest.txt')
#puts each line of text in the file as an string in a list
    lines = f.readlines()
#removes the header lines
    cutlines = lines[7:]
#returns the list of strings when this function is called
    return cutlines
    

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes('<html><head><meta name="color-scheme" content="light dark"></head>', "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
#specific formatting used by prometheus
        self.wfile.write(bytes('<pre style="word-wrap: break-word; white-space: pre-wrap;">', "utf-8"))

#each string in the list is cut to the desired offset and written followed by a line break
        for x in cutlines:
            keyvalue = x[71:].strip() + " " + x[51:55]
            self.wfile.write(bytes("%s" % keyvalue + '\n', "utf-8"))


        self.wfile.write(bytes("</pre>", "utf-8"))

        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == '__main__':

#makes the list a global variable
    cutlines = metricsscrape()

    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))
    

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")