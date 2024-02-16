
# BDN

Projeto pessoal para o curso de **Big Data para Negócios** para testar django do python.
Foi utilizado SB Admin v7.0.4 com bootstrap para auxiliar no design e layout.

### Exemplo de Estrutura para Menu sidenav

    SIDENAV = [
      { "type": "head", "name": "Core" },
      { "type": "item", "name": "Dashboard", "icon": "tachometer-alt", "link": "index.html" },
      { "type": "divi" },
      { "type": "head", "name": "Interface" },
      { "type": "menu", "name": "Layouts", "icon": "columns", "links": [
        { "desc": "Static Navigation", "link": "layout-static.html" }, 
        { "desc": "Light Sidenav", "link": "layout-sidenav-light.html" }, 
      ]},
      { "type": "nest", "name": "Pages", "icon": "book-open", "sub_itens": [
        { "name": "Authentication: ", "links": [
          { "desc": "Login", "link": "login.html" }, 
          { "desc": "Register", "link": "register.html" }, 
          { "desc": "Forgot Password", "link": "forgot-password.html" }, 
        ]}, 
        { "name": "Error:", "links": [
          { "desc": "401 Page", "link": "401.html" }, 
          { "desc": "404 Page", "link": "404.html" }, 
          { "desc": "500 Page", "link": "500.html" }, 
        ]}, 
      ]},
      { "type": "divi" },
      { "type": "head", "name": "Addons" },
      { "type": "item", "name": "Charts", "icon": "chart-area", "link": "charts.html" },
      { "type": "item", "name": "Tables", "icon": "table", "link": "tables.html" },
    ]
