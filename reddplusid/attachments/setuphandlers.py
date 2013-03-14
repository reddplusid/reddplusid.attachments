from collective.grok import gs
from reddplusid.attachments import MessageFactory as _

@gs.importstep(
    name=u'reddplusid.attachments', 
    title=_('reddplusid.attachments import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('reddplusid.attachments.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
