layui.define(['element', 'laytpl', 'home_http'], function(exports) {
    var element = layui.element
              ,$ = layui.jquery
           ,http = layui.home_http
         ,laytpl = layui.laytpl

    laytpl.config({
        open: '<%',
        close: '%>'
    })

    ~function() {
        storage = window.localStorage
        var pathname = null
        try {
            pathname = location.pathname.substr(1, location.pathname.length).split('/')
        } catch(err) {}

        if (pathname.length > 0 && pathname[0] != '') {
            if (pathname.length == 3) {
                var from_code = pathname[2]
                if (from_code == storage.getItem('code')) {
                    location.href = '/' + pathname[0] + '/steps'
                }
                http.get_code_exist(from_code, function(response) {
                    storage.setItem('from_code', pathname[2])
                }, function() {
                    location.href = '/' + pathname[0]
                })
            }

            var init_home = function(data) {
                var tpl = $('#layout-head-tpl').html()
                laytpl(tpl).render(data, function(html) {
                    $('#layout-head').html(html)
                })
            }

            var symbol = storage.getItem('symbol')
            var exist_team = JSON.parse(storage.getItem('team'))
            var exist_settings = JSON.parse(storage.getItem('settings'))
            var from_code = storage.getItem('from_code')

            if (symbol != null 
                && exist_settings != null 
                && exist_team != null 
                && exist_team.symbol == symbol 
                && symbol == pathname[0]) {

                data = JSON.parse(storage.getItem('settings'))
                init_home(data)

                return
            }

            http.get_team(pathname[0], function(response) {
                console.info(response)
                var team = response.team,
                settings = response.settings
                
                console.info(settings)

                storage.setItem('symbol', team.symbol)
                
                storage.setItem('team', JSON.stringify(team))
                storage.setItem('settings', JSON.stringify(settings))

                init_home(settings)
            })

        }
    }()

    exports('layout', {})
})
