from .views import HomeView, IndexView, GrubView, home_blueprint
from ..url_core import UrlRegister


class HomeUrlRegister(UrlRegister):
    def views_register():
        home_view = HomeView.as_view('home_view', template_name='home/home.html')
        index_view = IndexView.as_view('index_view', template_name='home/index.html')
        grub_view = GrubView.as_view('grub_view', template_name='home/home.html')

        home_blueprint.add_url_rule('/<string:symbol>',
                                    view_func=home_view,
                                    methods=['GET', ])

        home_blueprint.add_url_rule('/',
                                    view_func=index_view,
                                    methods=['GET', ])

        home_blueprint.add_url_rule('/<string:symbol>/s/<string:code>',
                                    view_func=grub_view,
                                    methods=['GET', ])
