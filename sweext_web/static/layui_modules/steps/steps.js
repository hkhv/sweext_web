layui.define(['base', 'laytpl', 'steps_http'], function(exports) {
    var $ = layui.jquery
   ,layer = layui.layer
  ,laytpl = layui.laytpl
    ,http = layui.steps_http
    ,base = layui.base

    laytpl.config({
        open: '<%',
        close: '%>'
    })

    storage = window.localStorage

    var code = storage.getItem('code')
    var settings = storage.getItem('settings')

    if (code == '' || code == null || settings == null) {
        storage.clear()
        location.href = '/ext'
    }

    settings = JSON.parse(settings)

    var init_steps_area = function() {
        settings.code = '/' + code
        settings.share_link = settings.share_link_domain + '/' + code

        http.get_invite_info(storage.getItem('code'), function(response) {
            settings.invited_count = response.invited
            settings.earned = response.earned
        }, function(response) {
            settings.invited_count = 0
            settings.earned = 0
        })

        var agent = window.navigator.userAgent.toLowerCase()

        if (agent.indexOf('mac') >= 0 || agent.indexOf('iphone') >= 0 || agent.indexOf('ipad') >= 0) {
            settings.is_iphone = true
        } else {
            settings.is_iphone = false 
        }

        var tpl = $('#steps-area-tpl').html()

        laytpl(tpl).render(settings, function(html) {
            $('#layout-body').html(html)
        })
    }

    init_steps_area()

    // **** init buttons **** {
    
    document.getElementById('copy-invite-code').onclick = function() {
        base.copy('#copy-code')
    }

    document.getElementById('copy-invite-link').onclick = function() {
        base.copy('#copy-link')
    }
    
    // } 

    exports('steps', {})
})
