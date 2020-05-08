import io

file = open("page.html","w")

file.writelines("<html>")
file.writelines("<body>")
file.writelines("<p>TESTE</p>")
file.writelines("</body></html>")

file.close()