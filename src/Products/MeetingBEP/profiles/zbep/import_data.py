# -*- coding: utf-8 -*-

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
agendaTemplate.pod_portal_types = ['MeetingBepCA']
agendaTemplate.tal_condition = u'python:tool.isManager(here)'

decisionsTemplate = PodTemplateDescriptor('pv', 'Procès-verbal')
decisionsTemplate.odt_file = 'pv.odt'
decisionsTemplate.pod_formats = ['odt', 'pdf', ]
decisionsTemplate.pod_portal_types = ['MeetingBepCA']
decisionsTemplate.tal_condition = u'python:tool.isManager(here)'

noteTravailTemplate = PodTemplateDescriptor('note-travail', 'Note de travail')
noteTravailTemplate.odt_file = 'notedetravail.odt'
noteTravailTemplate.pod_formats = ['odt', 'pdf', ]
noteTravailTemplate.pod_portal_types = ['MeetingItemBepCA']

extraitPVTemplate = PodTemplateDescriptor('extrait-pv', 'Extrait PV')
extraitPVTemplate.odt_file = 'extraitpv.odt'
extraitPVTemplate.pod_formats = ['odt', 'pdf', ]
extraitPVTemplate.pod_portal_types = ['MeetingItemBepCA']

templates = [agendaTemplate, decisionsTemplate, noteTravailTemplate, extraitPVTemplate]

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
dg_grp = GroupDescriptor('dirgen', 'Direction Générale', 'DG')
dg_grp.itemAdviceStates = (
    u'bep-audit__state__presented',
    u'bep-remun__state__presented',
    u'bep-ca__state__presented',
    u'crema-ca__state__presented',
    u'enviro-ca__state__presented',
    u'expa-ca__state__presented',
    u'idefin-ca__state__presented')
dg_grp.itemAdviceEditStates = (
    u'bep-audit__state__presented',
    u'bep-remun__state__presented',
    u'bep-ca__state__presented',
    u'crema-ca__state__presented',
    u'enviro-ca__state__presented',
    u'expa-ca__state__presented',
    u'idefin-ca__state__presented')
dg_grp.itemAdviceViewStates = (
    u'bep-audit__state__accepted',
    u'bep-audit__state__accepted_but_modified',
    u'bep-audit__state__pre_accepted',
    u'bep-audit__state__itemfrozen',
    u'bep-audit__state__presented',
    u'bep-audit__state__refused',
    u'bep-audit__state__returned_to_proposing_group',
    u'bep-audit__state__delayed',
    u'bep-remun__state__accepted',
    u'bep-remun__state__accepted_but_modified',
    u'bep-remun__state__pre_accepted',
    u'bep-remun__state__itemfrozen',
    u'bep-remun__state__presented',
    u'bep-remun__state__refused',
    u'bep-remun__state__returned_to_proposing_group',
    u'bep-remun__state__delayed',
    u'bep-ca__state__accepted',
    u'bep-ca__state__accepted_but_modified',
    u'bep-ca__state__pre_accepted',
    u'bep-ca__state__itemfrozen',
    u'bep-ca__state__presented',
    u'bep-ca__state__refused',
    u'bep-ca__state__returned_to_proposing_group',
    u'bep-ca__state__delayed',
    u'crema-ca__state__accepted',
    u'crema-ca__state__accepted_but_modified',
    u'crema-ca__state__pre_accepted',
    u'crema-ca__state__itemfrozen',
    u'crema-ca__state__presented',
    u'crema-ca__state__refused',
    u'crema-ca__state__returned_to_proposing_group',
    u'crema-ca__state__delayed',
    u'enviro-ca__state__accepted',
    u'enviro-ca__state__accepted_but_modified',
    u'enviro-ca__state__pre_accepted',
    u'enviro-ca__state__itemfrozen',
    u'enviro-ca__state__presented',
    u'enviro-ca__state__delayed',
    u'expa-ca__state__accepted',
    u'expa-ca__state__accepted_but_modified',
    u'expa-ca__state__pre_accepted',
    u'expa-ca__state__itemfrozen',
    u'expa-ca__state__presented',
    u'expa-ca__state__refused',
    u'expa-ca__state__returned_to_proposing_group',
    u'expa-ca__state__delayed',
    u'idefin-ca__state__accepted',
    u'idefin-ca__state__accepted_but_modified',
    u'idefin-ca__state__pre_accepted',
    u'idefin-ca__state__itemfrozen',
    u'idefin-ca__state__presented',
    u'idefin-ca__state__refused',
    u'idefin-ca__state__returned_to_proposing_group',
    u'idefin-ca__state__delayed')
sg_grp = GroupDescriptor('secretariat', 'Secrétariat Général', 'SG')
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
be_grp = GroupDescriptor('bureau-detudes', 'Bureau d\'Études', 'BE')
dt_grp = GroupDescriptor('developpement-territorial', 'Développement Territorial', 'DT')
mo_grp = GroupDescriptor('maitrise-douvrages', 'Maitrise d\'ouvrages', 'MO')
infra_grp = GroupDescriptor('infrastructure', 'Infrastructure', 'INFRA')
amt_grp = GroupDescriptor('amenagement-du-territoire', 'Aménagement du territoire', 'AMT')
ne_grp = GroupDescriptor('namur-expo', 'Namur Expo', 'EXPO')
crema_grp = GroupDescriptor('bep-crematorium', 'BEP Crématorium', 'CREMA')
idefin_grp = GroupDescriptor('idefin', 'Idefin', 'IDEFIN')
tlm_grp = GroupDescriptor('tout-le-monde', 'Tout le monde', 'TLM')
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
bepca.shortName = 'BepCA'
bepca.configGroup = 'bep'
bepca.podTemplates = templates
bepca.addContacts = True

# BEP - Audit
bepaudit = MeetingConfigDescriptor(
    'bep-audit', "Comité d'Audit", "Comité d'Audit", isDefault=False)
bepaudit = deepcopy(simple_import_data.simpleMeeting)
bepaudit.id = 'bep-audit'
bepaudit.title = "Comité d'Audit"
bepaudit.shortName = 'BepAudit'
bepaudit.configGroup = 'bep'
bepaudit.folderTitle = "Comité d'Audit"
bepaudit.podTemplates = []

# BEP - Rémunération
bepremun = MeetingConfigDescriptor(
    'bep-remun', "Comité de Rémunération", "Comité de Rémunération", isDefault=False)
bepremun = deepcopy(simple_import_data.simpleMeeting)
bepremun.id = 'bep-remun'
bepremun.title = "Comité de Rémunération"
bepremun.shortName = 'BepRemun'
bepremun.configGroup = 'bep'
bepremun.folderTitle = "Comité de Rémunération"
bepremun.podTemplates = []

# EXPA - CA
expaca = MeetingConfigDescriptor(
    'expa-ca', "Conseil d'Administration", "Conseil d'Administration", isDefault=False)
expaca = deepcopy(simple_import_data.simpleMeeting)
expaca.id = 'expa-ca'
expaca.title = "Conseil d'Administration"
expaca.folderTitle = "Conseil d'Administration"
expaca.shortName = 'ExpaCA'
expaca.configGroup = 'expa'
expaca.podTemplates = []

# ENVIRO - CA
enviroca = MeetingConfigDescriptor(
    'enviro-ca', "Conseil d'Administration", "Conseil d'Administration", isDefault=False)
enviroca = deepcopy(simple_import_data.simpleMeeting)
enviroca.id = 'enviro-ca'
enviroca.title = "Conseil d'Administration"
enviroca.folderTitle = "Conseil d'Administration"
enviroca.shortName = 'EnviroCA'
enviroca.configGroup = 'enviro'
enviroca.podTemplates = []

# CREMA - CA
cremaca = MeetingConfigDescriptor(
    'crema-ca', "Conseil d'Administration", "Conseil d'Administration", isDefault=False)
cremaca = deepcopy(simple_import_data.simpleMeeting)
cremaca.id = 'crema-ca'
cremaca.title = "Conseil d'Administration"
cremaca.folderTitle = "Conseil d'Administration"
cremaca.shortName = 'CremaCA'
cremaca.configGroup = 'crema'
cremaca.podTemplates = []

# IDEFIN - CA
idefinca = MeetingConfigDescriptor(
    'idefin-ca', "Conseil d'Administration", "Conseil d'Administration", isDefault=False)
idefinca = deepcopy(simple_import_data.simpleMeeting)
idefinca.id = 'idefin-ca'
idefinca.title = "Conseil d'Administration"
idefinca.folderTitle = "Conseil d'Administration"
idefinca.shortName = 'IdefinCA'
idefinca.configGroup = 'idefin'
idefinca.podTemplates = []

cfgs = (bepca, bepaudit, bepremun, expaca, enviroca, cremaca, idefinca)

for cfg in cfgs:
    # assembly and signatures
    cfg.certifiedSignatures = (
        {'function': 'Directeur, Secr\xc3\xa9tariat G\xc3\xa9n\xc3\xa9ral',
         'signatureNumber': '1',
         'date_from': '',
         'name': 'O. GRANVILLE',
         'date_to': ''},
        {'function': 'Le Signataire 2 FF',
         'signatureNumber': '2',
         'date_from': '',
         'name': 'Vraiment Exemple',
         'date_to': ''},
        {'function': 'Charg\xc3\xa9 de Mission',
         'signatureNumber': '3',
         'date_from': '',
         'name': 'S. TRIFFOY',
         'date_to': ''},
        {'function': 'Directeur, Secr\xc3\xa9tariat G\xc3\xa9n\xc3\xa9ral',
         'signatureNumber': '4',
         'date_from': '',
         'name': 'O. GRANVILLE',
         'date_to': ''})
    # data
    cfg.useGroupsAsCategories = False
    cfg.usedMeetingAttributes = ['startDate', 'endDate', 'attendees', 'excused',
                                 'signatories', 'replacements', 'place', 'observations', ]
    cfg.categories = categories

    # gui
    cfg.itemColumns = ('Creator', 'ModificationDate', 'review_state', 'getProposingGroup',
                       'advices', 'linkedMeetingDate', 'actions')
    cfg.meetingColumns = ('Creator', 'CreationDate', 'review_state', 'actions')
    cfg.meetingColumns = ('Creator', 'CreationDate', 'review_state', 'actions')
    cfg.itemsListVisibleColumns = ('Creator', 'ModificationDate', 'review_state',
                                   'getProposingGroup', 'advices', 'actions')
    cfg.availableItemsListVisibleColumns = ('Creator', 'ModificationDate',
                                            'getProposingGroup', 'advices', 'actions')
    cfg.dashboardItemsListingsFilters = (u'c4', u'c5', u'c6', u'c7', u'c8', u'c9', u'c10',
                                         u'c11', u'c12', u'c13', u'c14', u'c15', u'c16')
    cfg.dashboardMeetingAvailableItemsFilters = (u'c4', u'c7', u'c8', u'c11', u'c16')
    cfg.dashboardMeetingLinkedItemsFilters = (u'c4', u'c5', u'c6', u'c7',
                                              u'c11', u'c12', u'c16', u'c19')
    # workflow
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
    cfg.onTransitionFieldTransforms = (
        {'transition': 'validate',
         'field_name': 'MeetingItem.decision',
         'tal_expression': 'python: here.adapted().adaptDecisionClonedItem()'},)
    # advices and access
    cfg.usedAdviceTypes = (u'asked_again', u'positive', u'positive_with_remarks', u'negative', u'nil')
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
         'for_item_created_until': '',
         'group': 'coaching-entreprises-chef-de-service',
         'available_on': '',
         'delay': '',
         'gives_auto_advice_on_help_message': '',
         'gives_auto_advice_on': "python: item.getProposingGroup() == 'coaching-entreprises'",
         'delay_left_alert': '',
         'is_linked_to_previous_row': '0',
         'for_item_created_from': '2018/01/01',
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
    cfg.useCopies = True
    cfg.selectableCopyGroups = (
        u'dirgen_observers', u'dirgen_reviewers',
        u'secretariat_observers', u'secretariat_reviewers',
        u'communication_observers', u'communication_reviewers',
        u'service-juridique_observers', u'service-juridique_reviewers',
        u'finances-et-comptabilite_observers', u'finances-et-comptabilite_reviewers',
        u'ressources-humaines_observers', u'ressources-humaines_reviewers',
        u'ressources-humaines-confidentiel_observers', u'ressources-humaines-confidentiel_reviewers',
        u'services-generaux_observers', u'services-generaux_reviewers',
        u'informatique_observers', u'informatique_reviewers',
        u'developpement-economique_observers', u'developpement-economique_reviewers',
        u'coaching-entreprises_observers', u'coaching-entreprises_reviewers',
        u'attraction-investisseurs_observers', u'attraction-investisseurs_reviewers',
        u'animation-economique_observers', u'animation-economique_reviewers',
        u'intelligence-strategique_observers', u'intelligence-strategique_reviewers',
        u'environnement_observers', u'environnement_reviewers',
        u'facturation_observers', u'facturation_reviewers',
        u'collectes_observers', u'collectes_reviewers',
        u'parcs_observers', u'parcs_reviewers',
        u'bureau-detudes_observers', u'bureau-detudes_reviewers',
        u'developpement-territorial_observers', u'developpement-territorial_reviewers',
        u'maitrise-douvrages_observers', u'maitrise-douvrages_reviewers',
        u'infrastructure_observers', u'infrastructure_reviewers',
        u'amenagement-du-territoire_observers', u'amenagement-du-territoire_reviewers',
        u'namur-expo_observers', u'namur-expo_reviewers',
        u'bep-crematorium_observers', u'bep-crematorium_reviewers',
        u'idefin_observers', u'idefin_reviewers',
        u'coaching-entreprises-chef-de-service_observers',
        u'coaching-entreprises-chef-de-service_reviewers',
        u'tout-le-monde_observers', u'tout-le-monde_reviewers')
    cfg.itemCopyGroupsStates = (
        u'accepted', u'accepted_but_modified', u'accepted_out_of_meeting',
        u'accepted_out_of_meeting_emergency', u'pre_accepted',
        u'itemfrozen', u'refused', u'delayed')


data = PloneMeetingConfiguration(
    meetingFolderTitle='Mes séances',
    meetingConfigs=cfgs,
    groups=[
        dg_grp, sg_grp, com_grp, jur_grp, fin_grp, rh_grp, rhc_grp, sr_grp,
        info_grp, de_grp, ce_grp, cecs_grp, ai_grp, ae_grp, is_grp, env_grp, fact_grp,
        coll_grp, parsc_grp, be_grp, dt_grp, mo_grp, infra_grp, amt_grp, ne_grp,
        crema_grp, idefin_grp, tlm_grp])
data.enableUserPreferences = False
data.configGroups = (
    {'row_id': 'bep', 'label': 'BEP'},
    {'row_id': 'expa', 'label': 'EXPA'},
    {'row_id': 'enviro', 'label': 'ENVIRO'},
    {'row_id': 'crema', 'label': 'CREMA'},
    {'row_id': 'idefin', 'label': 'IDEFIN'},
)
# ------------------------------------------------------------------------------
