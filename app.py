import traceback
try:
    from Lotto.views.main_view import view
except Exception, ex:
    print traceback.format_exc()


view.load()

