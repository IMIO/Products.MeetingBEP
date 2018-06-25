# -*- coding: utf-8 -*-

from DateTime import DateTime
from copy import deepcopy

from Products.PloneMeeting.profiles import AnnexTypeDescriptor
from Products.PloneMeeting.profiles import CategoryDescriptor
from Products.PloneMeeting.profiles import GroupDescriptor
from Products.PloneMeeting.profiles import ItemAnnexTypeDescriptor
from Products.PloneMeeting.profiles import MeetingConfigDescriptor
from Products.PloneMeeting.profiles import PloneGroupDescriptor
from Products.PloneMeeting.profiles import PloneMeetingConfiguration
from Products.PloneMeeting.profiles import PodTemplateDescriptor
from Products.PloneMeeting.profiles import UserDescriptor
from Products.MeetingCommunes.profiles.simple import import_data as simple_import_data

today = DateTime().strftime('%Y/%m/%d')

# File types -------------------------------------------------------------------
annexe = ItemAnnexTypeDescriptor('annexe', 'Annexe', u'attach.png')
annexeDecision = ItemAnnexTypeDescriptor('annexeDecision', 'Annexe à la décision', u'attach.png',
                                         relatedTo='item_decision')
annexeAvis = AnnexTypeDescriptor('annexeAvis', 'Annexe à un avis', u'attach.png',
                                 relatedTo='advice')
annexeSeance = AnnexTypeDescriptor('annexe', 'Annexe', u'attach.png', relatedTo='meeting')

# Categories -------------------------------------------------------------------
categories = [
    CategoryDescriptor('approbation-pv',
                       "Approbation du procès verbal de la dernière réunion"),
    CategoryDescriptor('decision',
                       "Décision"),
    CategoryDescriptor('information-strategie',
                       "Information et Stratégie"),
    CategoryDescriptor('communication',
                       "Communication"),
]

# Pod templates ----------------------------------------------------------------
agendaTemplate = PodTemplateDescriptor('oj', 'Ordre du jour')
agendaTemplate.odt_file = 'oj.odt'
agendaTemplate.pod_formats = ['odt', 'pdf', ]
agendaTemplate.pod_portal_types = ['MeetingCA']
agendaTemplate.tal_condition = 'python:tool.isManager(here)'

decisionsTemplate = PodTemplateDescriptor('pv', 'Procès-verbal')
decisionsTemplate.odt_file = 'pv.odt'
decisionsTemplate.pod_formats = ['odt', 'pdf', ]
decisionsTemplate.pod_portal_types = ['MeetingCA']
decisionsTemplate.tal_condition = 'python:tool.isManager(here)'

itemTemplate = PodTemplateDescriptor('deliberation', 'Délibération')
itemTemplate.odt_file = 'deliberation.odt'
itemTemplate.pod_formats = ['odt', 'pdf', ]
itemTemplate.pod_portal_types = ['MeetingItemCA']
itemTemplate.tal_condition = 'python:here.hasMeeting()'

templates = [agendaTemplate, decisionsTemplate, itemTemplate]

# Users ------------------------------------------------------------------------
ajo = UserDescriptor('ajo', [], email="ajo@bep.be", fullname="Amélie JOLY")
cbo = UserDescriptor('cbo', [], email="cbo@bep.be", fullname="Charlotte BOUILLET")
dlo = UserDescriptor('dlo', [], email="dlo@bep.be", fullname="David LONGFILS")
dma = UserDescriptor('dma', [], email="dma@bep.be", fullname="Delphine MAROT")
dde = UserDescriptor('dde', [], email="dde@bep.be", fullname="Dominique DETHY")
ebe = UserDescriptor('ebe', [], email="ebe@bep.be", fullname="Elisabeth BOIS D'ENGHIEN")
fma = UserDescriptor('fma', [], email="fma@bep.be", fullname="Frédéric MASSON")
gqu = UserDescriptor('gqu', [], email="gqu@bep.be", fullname="Geoffroy QUENON")
ito = UserDescriptor('ito', [], email="ito@bep.be", fullname="Imane TORY")
ibe = UserDescriptor('ibe', [], email="ibe@bep.be", fullname="Ingrid BERTRAND")
jyp = UserDescriptor('jyp', [], email="jyp@bep.be", fullname="Jean-Yves PAGES")
jpo = UserDescriptor('jpo', [], email="jpo@bep.be", fullname="Julien PONCELET")
jca = UserDescriptor('jca', [], email="jca@bep.be", fullname="Justine CAVILLOT")
lgo = UserDescriptor('lgo', [], email="lgo@bep.be", fullname="Laurence GOURGUE")
mdh = UserDescriptor('mdh', [], email="mdh@bep.be", fullname="Marc DEHARENG")
mdr = UserDescriptor('mdr', [], email="mdr@bep.be", fullname="Marc DERROITTE")
mdu = UserDescriptor('mdu', [], email="mdu@bep.be", fullname="Marie DUPONT")
nvg = UserDescriptor('nvg', [], email="nvg@bep.be", fullname="Nathalie VAN GOEY ")
ogr = UserDescriptor('ogr', [], email="ogr@bep.be", fullname="Olivier GRANVILLE")
pli = UserDescriptor('pli', [], email="pli@bep.be", fullname="Pascal LIBOIS")
qox = UserDescriptor('qox', [], email="qox@bep.be", fullname="Quentin ORBAN DE XIVRY")
rde = UserDescriptor('rde', [], email="rde@bep.be", fullname="Renaud DEGUELDRE")
sbr = UserDescriptor('sbr', [], email="sbr@bep.be", fullname="Sébastien BOURGEOIS")
str_user = UserDescriptor('str', [], email="str@bep.be", fullname="Sébastien TRIFFOY")
sma = UserDescriptor('sma', [], email="sma@bep.be", fullname="Sophie MARLET")
the = UserDescriptor('the', [], email="the@bep.be", fullname="Tom HEURION")
isa = UserDescriptor('isa', [], email="isa@bep.be", fullname="Isabelle SADIN")
assembly_member = UserDescriptor('assembly_member', [], email="test@test.be", fullname="Assembly Member")

# Groups -----------------------------------------------------------------------
dg_grp = GroupDescriptor('direction-generale', 'Direction Générale', 'DG')
sg_grp = GroupDescriptor('secretarit-general', 'Secrétariat Général', 'SG')
com_grp = GroupDescriptor('communication', 'Communication', 'COM')
jur_grp = GroupDescriptor('service-juridique', 'Service Juridique', 'JUR')
jur_grp.itemAdviceStates = (
        'bep-codir__state__presented',
        'bep-codir__state__returned_to_proposing_group',
        'bep-codir__state__validated',
        'bep-ca__state__presented',
        'bep-ca__state__returned_to_proposing_group',
        'bep-ca__state__validated')
jur_grp.itemAdviceEditStates = (
        'bep-codir__state__presented',
        'bep-codir__state__returned_to_proposing_group',
        'bep-codir__state__validated',
        'bep-ca__state__presented',
        'bep-ca__state__returned_to_proposing_group',
        'bep-ca__state__validated')
jur_grp.itemAdviceViewStates = (
        'bep-codir__state__accepted',
        'bep-codir__state__accepted_but_modified',
        'bep-codir__state__pre_accepted',
        'bep-codir__state__itemfrozen',
        'bep-codir__state__presented',
        'bep-codir__state__refused',
        'bep-codir__state__returned_to_proposing_group',
        'bep-codir__state__delayed',
        'bep-codir__state__validated',
        'bep-ca__state__accepted',
        'bep-ca__state__accepted_but_modified',
        'bep-ca__state__accepted_out_of_meeting',
        'bep-ca__state__accepted_out_of_meeting_emergency',
        'bep-ca__state__pre_accepted',
        'bep-ca__state__itemfrozen',
        'bep-ca__state__presented',
        'bep-ca__state__refused',
        'bep-ca__state__returned_to_proposing_group',
        'bep-ca__state__delayed',
        'bep-ca__state__validated')
fin_grp = GroupDescriptor('finances-et-comptabilite', 'Finances et Comptabilité', 'FIN')
fin_grp.itemAdviceStates = (
        'bep-codir__state__presented',
        'bep-codir__state__returned_to_proposing_group',
        'bep-codir__state__validated',
        'bep-ca__state__presented',
        'bep-ca__state__returned_to_proposing_group',
        'bep-ca__state__validated')
fin_grp.itemAdviceEditStates = (
        'bep-codir__state__presented',
        'bep-codir__state__returned_to_proposing_group',
        'bep-codir__state__validated',
        'bep-ca__state__presented',
        'bep-ca__state__returned_to_proposing_group',
        'bep-ca__state__validated')
fin_grp.itemAdviceViewStates = (
        'bep-codir__state__accepted',
        'bep-codir__state__accepted_but_modified',
        'bep-codir__state__pre_accepted',
        'bep-codir__state__itemfrozen',
        'bep-codir__state__presented',
        'bep-codir__state__refused',
        'bep-codir__state__returned_to_proposing_group',
        'bep-codir__state__delayed',
        'bep-codir__state__validated',
        'bep-ca__state__accepted',
        'bep-ca__state__accepted_but_modified',
        'bep-ca__state__accepted_out_of_meeting',
        'bep-ca__state__accepted_out_of_meeting_emergency',
        'bep-ca__state__pre_accepted',
        'bep-ca__state__itemfrozen',
        'bep-ca__state__presented',
        'bep-ca__state__refused',
        'bep-ca__state__returned_to_proposing_group',
        'bep-ca__state__delayed',
        'bep-ca__state__validated')
rh_grp = GroupDescriptor('ressources-humaines', 'Ressources Humaines', 'RH')
rhc_grp = GroupDescriptor('ressources-humaines-confidentiel', 'Ressources Humaines (Confidentiel)', 'RHC')
sr_grp = GroupDescriptor('services-generaux', 'Services Généraux', 'SG')
info_grp = GroupDescriptor('informatique', 'Informatique', 'INFO')
de_grp = GroupDescriptor('developpement-economique', 'Développement Économiqe', 'DE')
ce_grp = GroupDescriptor('coaching-entreprises', 'Coaching Entreprises', 'CE')
cecs_grp = GroupDescriptor('coaching-entreprises-chef-de-service', 'Coaching Entreprises (Chef de service)', 'CECS')
cecs_grp.itemAdviceStates = (
    'bep-codir__state__proposed',
    'bep-ca__state__proposed')
cecs_grp.itemAdviceEditStates = (
    'bep-codir__state__proposed',
    'bep-ca__state__proposed')
cecs_grp.itemAdviceViewStates = (
    'bep-codir__state__accepted',
    'bep-codir__state__accepted_but_modified',
    'bep-codir__state__pre_accepted',
    'bep-codir__state__itemfrozen',
    'bep-codir__state__proposed',
    'bep-codir__state__presented',
    'bep-codir__state__refused',
    'bep-codir__state__returned_to_proposing_group',
    'bep-codir__state__delayed',
    'bep-codir__state__validated',
    'bep-ca__state__accepted',
    'bep-ca__state__accepted_but_modified',
    'bep-ca__state__pre_accepted',
    'bep-ca__state__itemfrozen',
    'bep-ca__state__proposed',
    'bep-ca__state__presented',
    'bep-ca__state__refused',
    'bep-ca__state__returned_to_proposing_group',
    'bep-ca__state__delayed',
    'bep-ca__state__validated')
ai_grp = GroupDescriptor('attraction-investisseurs', 'Attraction Investisseurs', 'AI')
ae_grp = GroupDescriptor('animation-economique', 'Animation Économique', 'AE')
is_grp = GroupDescriptor('intelligence-strategique', 'Intelligence Stratégique', 'IS')
env_grp = GroupDescriptor('environnement', 'Environnement', 'ENV')
fact_grp = GroupDescriptor('facturation', 'Facturation', 'FACT')
coll_grp = GroupDescriptor('collectes', 'Collectes', 'COLL')
parsc_grp = GroupDescriptor('parcs', 'Parcs', 'PARCS')
be_grp = GroupDescriptor('bureau-d-etudes', 'Bureau d\'Études', 'BE')
dt_grp = GroupDescriptor('developpement-territorial', 'Développement Territorial', 'DT')
ne_grp = GroupDescriptor('namur-expo', 'Namur Expo', 'EXPO')
crema_grp = GroupDescriptor('bep-crematorium', 'BEP Crématorium', 'CREMA')
idefin_grp = GroupDescriptor('idefin', 'Idefin', 'IDEFIN')
ca_powerobservers = PloneGroupDescriptor('meeting-config-ca_powerobservers',
                                         'meeting-config-ca_powerobservers',
                                         [])
assembly_member.ploneGroups = [ca_powerobservers]

dg_grp.advisers.append(rde)
dg_grp.creators.append(rde)
dg_grp.reviewers.append(rde)

sg_grp.advisers.append(ogr)
sg_grp.creators += [ito, jca, ogr, str_user]
sg_grp.reviewers.append(ogr)

com_grp.advisers += [ibe, sma]
com_grp.creators += [ibe, sma]
com_grp.reviewers += [ibe, sma]

jur_grp.advisers += [ajo, mdu]
jur_grp.creators += [ajo, mdu]
jur_grp.reviewers += [ajo]

fin_grp.advisers += [ajo, fma, mdu]
fin_grp.creators += [ajo, fma, mdu]
fin_grp.reviewers += [ajo, fma]

info_grp.advisers += [gqu, jyp, mdr, pli, sbr, the]
info_grp.creators += [gqu, jyp, mdr, pli, sbr, the]
info_grp.reviewers += [mdr]

ce_grp.advisers += [cbo, dlo, dma, dde, ebe, jpo, lgo, mdh, nvg, qox]
ce_grp.creators += [cbo, dlo, dma, dde, ebe, jpo, lgo, mdh, nvg, qox]
ce_grp.reviewers += [lgo]
cecs_grp.advisers += [dma]

rh_grp.advisers = [isa]
rh_grp.creators = [isa]
rh_grp.reviewers = [isa]
rhc_grp.advisers = [isa]
rhc_grp.creators = [isa]
rhc_grp.reviewers = [isa]

# Meeting configurations -------------------------------------------------------
# BEP - CA
bepca = MeetingConfigDescriptor(
    'bep-ca', "Conseil d'Administration", "Conseil d'Administration", isDefault=True)
bepca = deepcopy(simple_import_data.simpleMeeting)
bepca.id = 'bep-ca'
bepca.title = "Conseil d'Administration"
bepca.folderTitle = "Conseil d'Administration"
bepca.shortName = 'CA'
bepca.configGroup = 'bep'
bepca.podTemplates = templates

# BEP - CODIR
bepcodir = MeetingConfigDescriptor(
    'bep-codir', "Comité de Direction", "Comité de Direction", isDefault=True)
bepcodir = deepcopy(simple_import_data.simpleMeeting)
bepcodir.id = 'bep-codir'
bepcodir.title = "Comité de Direction"
bepcodir.shortName = 'CoDir'
bepcodir.configGroup = 'bep'
bepcodir.folderTitle = "Comité de Direction"
bepcodir.podTemplates = []
bepcodir.addContacts = True

for cfg in (bepca, bepcodir):
    cfg.usedMeetingAttributes = ['startDate', 'endDate', 'attendees', 'excused', 'absents',
                                 'signatories', 'replacements', 'place', 'observations', ]
    cfg.categories = categories
    cfg.useGroupsAsCategories = False
    cfg.workflowAdaptations = (
        u'no_global_observation', u'no_publication',
        u'presented_item_back_to_proposed', u'return_to_proposing_group',
        u'accepted_out_of_meeting', u'accepted_out_of_meeting_emergency_and_duplicated',
        u'refused')
    cfg.itemConditionsInterface = 'Products.MeetingBEP.interfaces.IMeetingItemBEPWorkflowConditions'
    cfg.itemActionsInterface = 'Products.MeetingBEP.interfaces.IMeetingItemBEPWorkflowActions'
    cfg.meetingConditionsInterface = 'Products.MeetingBEP.interfaces.IMeetingBEPWorkflowConditions'
    cfg.meetingActionsInterface = 'Products.MeetingBEP.interfaces.IMeetingBEPWorkflowActions'
    cfg.itemDecidedStates = (
        u'accepted', u'accepted_but_modified', u'accepted_out_of_meeting',
        u'accepted_out_of_meeting_emergency', u'pre_accepted', u'refused', u'delayed')
    cfg.itemPositiveDecidedStates = (
        u'accepted', u'accepted_but_modified', u'accepted_out_of_meeting',
        u'accepted_out_of_meeting_emergency', u'pre_accepted')
    cfg.enableAdviceConfidentiality = True
    cfg.adviceConfidentialityDefault = True
    cfg.itemRestrictedPowerObserversStates = (
        u'accepted', u'accepted_but_modified', u'pre_accepted',
        u'itemfrozen', u'refused', u'returned_to_proposing_group',
        u'delayed')
    cfg.meetingRestrictedPowerObserversStates = (u'closed', u'decided', u'frozen')
    cfg.adviceConfidentialFor = ('restricted_power_observers', )
    cfg.hideHistoryTo = ('restricted_power_observers', )
    cfg.customAdvisers = ((
        {'delay_label': '',
         'for_item_created_until': '2018/01/01',
         'group': 'coaching-entreprises-chef-de-service',
         'available_on': '',
         'delay': '',
         'gives_auto_advice_on_help_message': '',
         'gives_auto_advice_on': "python: item.getProposingGroup() == 'coaching-entreprises'",
         'delay_left_alert': '',
         'is_linked_to_previous_row': '0',
         'for_item_created_from': today,
         'row_id': 'row_id_1'},
        {'delay_label': '',
         'for_item_created_until': '',
         'group': 'service-juridique',
         'available_on': '',
         'delay': '',
         'gives_auto_advice_on_help_message': '',
         'gives_auto_advice_on': "python: True",
         'delay_left_alert': '',
         'is_linked_to_previous_row': '0',
         'for_item_created_from': '2018/01/01',
         'row_id': 'row_id_2'},
        {'delay_label': '',
         'for_item_created_until': '',
         'group': 'finances-et-comptabilite',
         'available_on': '',
         'delay': '',
         'gives_auto_advice_on_help_message': '',
         'gives_auto_advice_on': "python: True",
         'delay_left_alert': '',
         'is_linked_to_previous_row': '0',
         'for_item_created_from': '2018/01/01',
         'row_id': 'row_id_2'}, ))
    cfg.onTransitionFieldTransforms = (
        {'transition': 'validate',
         'field_name': 'MeetingItem.decision',
         'tal_expression': 'python: here.adapted().adaptDecisionClonedItem()'},)

data = PloneMeetingConfiguration(
    meetingFolderTitle='Mes séances',
    meetingConfigs=(bepcodir, bepca),
    groups=[
        dg_grp, sg_grp, com_grp, jur_grp, fin_grp, rh_grp, rhc_grp, sr_grp,
        info_grp, de_grp, ce_grp, cecs_grp, ai_grp, ae_grp, is_grp, env_grp, fact_grp,
        coll_grp, parsc_grp, be_grp, dt_grp, ne_grp, crema_grp, idefin_grp])
data.enableUserPreferences = False
data.configGroups = (
    {'row_id': 'bep', 'label': 'BEP'},
    {'row_id': 'expa', 'label': 'EXPA'},
    {'row_id': 'enviro', 'label': 'ENVIRO'},
    {'row_id': 'crema', 'label': 'CREMA'},
    {'row_id': 'idefin', 'label': 'IDEFIN'},
)
# ------------------------------------------------------------------------------