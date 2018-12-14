# -*- coding: utf-8 -*-

from copy import deepcopy

from Products.PloneMeeting.profiles import AnnexTypeDescriptor
from Products.PloneMeeting.profiles import CategoryDescriptor
from Products.PloneMeeting.profiles import OrgDescriptor
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
                       "Approbation du procès verbal de la dernière réunion",
                       usingGroups=['dirgen', 'secretariat']),
    CategoryDescriptor('decision',
                       "Décision"),
    CategoryDescriptor('communication',
                       "Communication"),
]

# Pod templates ----------------------------------------------------------------
agendaTemplate = PodTemplateDescriptor('oj', 'Ordre du jour')
agendaTemplate.is_reusable = True
agendaTemplate.odt_file = 'oj.odt'
agendaTemplate.pod_formats = ['odt', 'pdf', ]
agendaTemplate.pod_portal_types = ['Meeting']
agendaTemplate.tal_condition = u'python:tool.isManager(here)'

decisionsTemplate = PodTemplateDescriptor('pv', 'Procès-verbal')
decisionsTemplate.is_reusable = True
decisionsTemplate.odt_file = 'pv.odt'
decisionsTemplate.pod_formats = ['odt', 'pdf', ]
decisionsTemplate.pod_portal_types = ['Meeting']
decisionsTemplate.tal_condition = u'python:tool.isManager(here)'

noteTravailTemplate = PodTemplateDescriptor('note-travail', 'Note de travail')
noteTravailTemplate.is_reusable = True
noteTravailTemplate.odt_file = 'notedetravail.odt'
noteTravailTemplate.pod_formats = ['odt', 'pdf', ]
noteTravailTemplate.pod_portal_types = ['MeetingItem']

extraitPVTemplate = PodTemplateDescriptor('extrait-pv', 'Extrait PV')
extraitPVTemplate.is_reusable = True
extraitPVTemplate.odt_file = 'extraitpv.odt'
extraitPVTemplate.pod_formats = ['odt', 'pdf', ]
extraitPVTemplate.pod_portal_types = ['MeetingItem']
extraitPVTemplate.tal_condition = u'python:tool.isManager(here)'

templates = [agendaTemplate, decisionsTemplate, noteTravailTemplate, extraitPVTemplate]

reuseAgendaTemplate = PodTemplateDescriptor('oj', 'Ordre du jour')
reuseAgendaTemplate.pod_template_to_use = {'cfg_id': 'bep-ca', 'template_id': 'oj'}
reuseAgendaTemplate.pod_formats = ['odt', 'pdf', ]
reuseAgendaTemplate.pod_portal_types = ['Meeting']
reuseAgendaTemplate.tal_condition = u'python:tool.isManager(here)'

reuseDecisionsTemplate = PodTemplateDescriptor('pv', 'Procès-verbal')
reuseDecisionsTemplate.pod_template_to_use = {'cfg_id': 'bep-ca', 'template_id': 'pv'}
reuseDecisionsTemplate.pod_formats = ['odt', 'pdf', ]
reuseDecisionsTemplate.pod_portal_types = ['Meeting']
reuseDecisionsTemplate.tal_condition = u'python:tool.isManager(here)'

reuseNoteTravailTemplate = PodTemplateDescriptor('note-travail', 'Note de travail')
reuseNoteTravailTemplate.pod_template_to_use = {'cfg_id': 'bep-ca', 'template_id': 'note-travail'}
reuseNoteTravailTemplate.pod_formats = ['odt', 'pdf', ]
reuseNoteTravailTemplate.pod_portal_types = ['MeetingItem']

reuseExtraitPVTemplate = PodTemplateDescriptor('extrait-pv', 'Extrait PV')
reuseExtraitPVTemplate.pod_template_to_use = {'cfg_id': 'bep-ca', 'template_id': 'extrait-pv'}
reuseExtraitPVTemplate.pod_formats = ['odt', 'pdf', ]
reuseExtraitPVTemplate.pod_portal_types = ['MeetingItem']
reuseExtraitPVTemplate.tal_condition = u'python:tool.isManager(here)'

reuse_templates = [reuseAgendaTemplate, reuseDecisionsTemplate,
                   reuseNoteTravailTemplate, reuseExtraitPVTemplate]

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
dg_org = OrgDescriptor('dirgen', u'Direction Générale', u'DG')
sg_org = OrgDescriptor('secretariat', u'Secrétariat Général', u'SECGEN')
sgcs_org = OrgDescriptor('secretariat-general-chef-de-service',
                         u'Secrétariat Général (Chef de service)',
                         u'SECGEN (chef de service)')
com_org = OrgDescriptor('communication', u'Communication', u'COM')
comcs_org = OrgDescriptor('communication-web-chef-de-service',
                          u'Communication & Web (Chef de service)',
                          u'Com & Web (chef)')
jur_org = OrgDescriptor('service-juridique', u'Service Juridique', u'JUR')
jur_org.item_advice_states = [
    'bep-codir__state__presented',
    'bep-codir__state__validated',
    'bep-ca__state__presented',
    'bep-ca__state__validated']
jur_org.item_advice_edit_states = [
    'bep-codir__state__presented',
    'bep-codir__state__validated',
    'bep-ca__state__presented',
    'bep-ca__state__validated']
jur_org.item_advice_view_states = [
    'bep-codir__state__accepted',
    'bep-codir__state__accepted_but_modified',
    'bep-codir__state__pre_accepted',
    'bep-codir__state__itemfrozen',
    'bep-codir__state__presented',
    'bep-codir__state__refused',
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
    'bep-ca__state__delayed',
    'bep-ca__state__validated']
fin_org = OrgDescriptor('finances-et-comptabilite', u'Finances et Comptabilité', u'FIN')
fin_org.item_advice_states = [
    'bep-codir__state__presented',
    'bep-codir__state__validated',
    'bep-ca__state__presented',
    'bep-ca__state__validated']
fin_org.item_advice_edit_states = [
    'bep-codir__state__presented',
    'bep-codir__state__validated',
    'bep-ca__state__presented',
    'bep-ca__state__validated']
fin_org.item_advice_view_states = [
    'bep-codir__state__accepted',
    'bep-codir__state__accepted_but_modified',
    'bep-codir__state__pre_accepted',
    'bep-codir__state__itemfrozen',
    'bep-codir__state__presented',
    'bep-codir__state__refused',
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
    'bep-ca__state__delayed',
    'bep-ca__state__validated']
log_org = OrgDescriptor('logistique', u'Logistique & Recyparcs', u'Logistic & Recyparc')
logcs_org = OrgDescriptor('logistic-recyparcs-chef-de-serivce',
                          u'Logistique & Recyparcs (Chef de service)',
                          u'Logistic & recyparc (chef)')
rhc_org = OrgDescriptor('ressources-humaines-confidentiel', u'Ressources Humaines (Confidentiel)', u'RHC')
sr_org = OrgDescriptor('services-generaux', u'Services Généraux', u'SG')
info_org = OrgDescriptor('informatique', u'Informatique', u'INFO')
de_org = OrgDescriptor('developpement-economique', u'Développement Économiqe', u'DE')
ce_org = OrgDescriptor('coaching-entreprises', u'Coaching Entreprises', u'CE')
cecs_org = OrgDescriptor('coaching-entreprises-chef-de-service', u'Coaching Entreprises (Chef de service)', u'CECS')
ai_org = OrgDescriptor('attraction-investisseurs', u'Attraction Investisseurs', u'AI')
ae_org = OrgDescriptor('animation-economique', u'Animation Économique', u'AE')
is_org = OrgDescriptor('intelligence-strategique', u'Intelligence Stratégique', u'IS')
env_org = OrgDescriptor('environnement', u'Environnement', u'ENV')
fact_org = OrgDescriptor('facturation', u'Facturation', u'FACT')
coll_org = OrgDescriptor('collectes', u'Collectes', u'COLL')
parsc_org = OrgDescriptor('parcs', u'Parcs', u'PARCS')
ti_org = OrgDescriptor('traitement-industriel',
                       u'Traitement industriel & études de projets',
                       u'Traitement ind et étude projets')
tics_org = OrgDescriptor('traitement-industriel-etudes-de-projets-chef-de-service',
                         u'Traitement industriel & études de projets (Chef de service)',
                         u'')
dt_org = OrgDescriptor('developpement-territorial', u'Développement Territorial', u'DT')
mo_org = OrgDescriptor('maitrise-douvrages', u'Maitrise d\'ouvrages', u'MO')
mocs_org = OrgDescriptor('maitrise-douvrage-chef-de-service',
                         u'Maitrise d\'ouvrages (Chef de service)',
                         u'Maîtrise (chef)')
infra_org = OrgDescriptor('infrastructure', u'Infrastructure', u'INFRA')
amt_org = OrgDescriptor('amenagement-du-territoire', u'Aménagement du territoire', u'AMT')
ne_org = OrgDescriptor('namur-expo', u'Namur Expo', u'EXPO')
crema_org = OrgDescriptor('bep-crematorium', u'BEP Crématorium', u'CREMA')
idefin_org = OrgDescriptor('idefin', u'Idefin', u'IDEFIN')
ca_restrictedpowerobservers = PloneGroupDescriptor(
    'meeting-config-ca_restrictedpowerobservers',
    'meeting-config-ca_restrictedpowerobservers',
    [])
assembly_member.ploneGroups = [ca_restrictedpowerobservers]

dg_org.advisers.append(rde)
dg_org.creators.append(rde)
dg_org.reviewers.append(rde)

sg_org.advisers.append(ogr)
sg_org.creators += [ito, jca, ogr, str_user]
sg_org.reviewers.append(ogr)
sgcs_org.advisers.append(ogr)

com_org.advisers += [ibe, sma]
com_org.creators += [ibe, sma]
com_org.reviewers += [ibe, sma]

jur_org.advisers += [ajo, mdu]
jur_org.creators += [ajo, mdu]
jur_org.reviewers += [ajo]

fin_org.advisers += [ajo, fma, mdu]
fin_org.creators += [ajo, fma, mdu]
fin_org.reviewers += [ajo, fma]

info_org.advisers += [gqu, jyp, mdr, pli, sbr, the]
info_org.creators += [gqu, jyp, mdr, pli, sbr, the]
info_org.reviewers += [mdr]

ce_org.advisers += [cbo, dlo, dma, dde, ebe, jpo, lgo, mdh, nvg, qox]
ce_org.creators += [cbo, dlo, dma, dde, ebe, jpo, lgo, mdh, nvg, qox]
ce_org.reviewers += [lgo]
cecs_org.advisers += [dma]

rhc_org.advisers = [isa]
rhc_org.creators = [isa]
rhc_org.reviewers = [isa]

# Meeting configurations -------------------------------------------------------
# BEP - CA
bepca = deepcopy(simple_import_data.simpleMeeting)
bepca.id = 'bep-ca'
bepca.title = "Conseil d'Administration"
bepca.folderTitle = "Conseil d'Administration"
bepca.shortName = 'BepCA'
bepca.configGroup = 'bep'
bepca.podTemplates = templates
bepca.addContacts = True

# BEP - Audit
bepaudit = deepcopy(simple_import_data.simpleMeeting)
bepaudit.id = 'bep-audit'
bepaudit.title = "Comité d'Audit"
bepaudit.shortName = 'BepAudit'
bepaudit.configGroup = 'bep'
bepaudit.folderTitle = "Comité d'Audit"
bepaudit.podTemplates = reuse_templates

# BEP - Rémunération
bepremun = deepcopy(simple_import_data.simpleMeeting)
bepremun.id = 'bep-remun'
bepremun.title = "Comité de Rémunération"
bepremun.shortName = 'BepRemun'
bepremun.configGroup = 'bep'
bepremun.folderTitle = "Comité de Rémunération"
bepremun.podTemplates = reuse_templates

# BEP - AG
bepag = deepcopy(simple_import_data.simpleMeeting)
bepag.id = 'bep-ag'
bepag.title = "Assemblée Générale"
bepag.shortName = 'BepAG'
bepag.configGroup = 'bep'
bepag.folderTitle = "Assemblée Générale"
bepag.podTemplates = reuse_templates

# EXPA - CA
expaca = deepcopy(simple_import_data.simpleMeeting)
expaca.id = 'expa-ca'
expaca.title = "Conseil d'Administration"
expaca.folderTitle = "Conseil d'Administration"
expaca.shortName = 'ExpaCA'
expaca.configGroup = 'expa'
expaca.podTemplates = reuse_templates

# EXPA - Audit
expaaudit = deepcopy(simple_import_data.simpleMeeting)
expaaudit.id = 'expa-audit'
expaaudit.title = "Comité d'Audit"
expaaudit.shortName = 'ExpaAudit'
expaaudit.configGroup = 'expa'
expaaudit.folderTitle = "Comité d'Audit"
expaaudit.podTemplates = reuse_templates

# EXPA - Rémunération
exparemun = deepcopy(simple_import_data.simpleMeeting)
exparemun.id = 'expa-remun'
exparemun.title = "Comité de Rémunération"
exparemun.shortName = 'ExpaRemun'
exparemun.configGroup = 'expa'
exparemun.folderTitle = "Comité de Rémunération"
exparemun.podTemplates = reuse_templates

# EXPA - AG
expaag = deepcopy(simple_import_data.simpleMeeting)
expaag.id = 'expa-ag'
expaag.title = "Assemblée Générale"
expaag.shortName = 'ExpaAG'
expaag.configGroup = 'expa'
expaag.folderTitle = "Assemblée Générale"
expaag.podTemplates = reuse_templates

# ENVIRO - CA
enviroca = deepcopy(simple_import_data.simpleMeeting)
enviroca.id = 'enviro-ca'
enviroca.title = "Conseil d'Administration"
enviroca.folderTitle = "Conseil d'Administration"
enviroca.shortName = 'EnviroCA'
enviroca.configGroup = 'enviro'
enviroca.podTemplates = reuse_templates

# ENVIRO - Audit
enviroaudit = deepcopy(simple_import_data.simpleMeeting)
enviroaudit.id = 'enviro-audit'
enviroaudit.title = "Comité d'Audit"
enviroaudit.shortName = 'EnviroAudit'
enviroaudit.configGroup = 'enviro'
enviroaudit.folderTitle = "Comité d'Audit"
enviroaudit.podTemplates = reuse_templates

# ENVIRO - Rémunération
enviroremun = deepcopy(simple_import_data.simpleMeeting)
enviroremun.id = 'enviro-remun'
enviroremun.title = "Comité de Rémunération"
enviroremun.shortName = 'EnviroRemun'
enviroremun.configGroup = 'enviro'
enviroremun.folderTitle = "Comité de Rémunération"
enviroremun.podTemplates = reuse_templates

# ENVIRO - AG
enviroag = deepcopy(simple_import_data.simpleMeeting)
enviroag.id = 'enviro-ag'
enviroag.title = "Assemblée Générale"
enviroag.shortName = 'EnviroAG'
enviroag.configGroup = 'enviro'
enviroag.folderTitle = "Assemblée Générale"
enviroag.podTemplates = reuse_templates

# CREMA - CA
cremaca = deepcopy(simple_import_data.simpleMeeting)
cremaca.id = 'crema-ca'
cremaca.title = "Conseil d'Administration"
cremaca.folderTitle = "Conseil d'Administration"
cremaca.shortName = 'CremaCA'
cremaca.configGroup = 'crema'
cremaca.podTemplates = reuse_templates

# CREMA - Audit
cremaaudit = deepcopy(simple_import_data.simpleMeeting)
cremaaudit.id = 'crema-audit'
cremaaudit.title = "Comité d'Audit"
cremaaudit.shortName = 'CremaAudit'
cremaaudit.configGroup = 'crema'
cremaaudit.folderTitle = "Comité d'Audit"
cremaaudit.podTemplates = reuse_templates

# CREMA - Rémunération
cremaremun = deepcopy(simple_import_data.simpleMeeting)
cremaremun.id = 'crema-remun'
cremaremun.title = "Comité de Rémunération"
cremaremun.shortName = 'CremaRemun'
cremaremun.configGroup = 'crema'
cremaremun.folderTitle = "Comité de Rémunération"
cremaremun.podTemplates = reuse_templates

# CREMA - AG
cremaag = deepcopy(simple_import_data.simpleMeeting)
cremaag.id = 'crema-ag'
cremaag.title = "Assemblée Générale"
cremaag.shortName = 'CremaAG'
cremaag.configGroup = 'crema'
cremaag.folderTitle = "Assemblée Générale"
cremaag.podTemplates = reuse_templates

# IDEFIN - CA
idefinca = MeetingConfigDescriptor(
    'idefin-ca', "Conseil d'Administration", "Conseil d'Administration", isDefault=False)
idefinca = deepcopy(simple_import_data.simpleMeeting)
idefinca.id = 'idefin-ca'
idefinca.title = "Conseil d'Administration"
idefinca.folderTitle = "Conseil d'Administration"
idefinca.shortName = 'IdefinCA'
idefinca.configGroup = 'idefin'
idefinca.podTemplates = reuse_templates

# IDEFIN - Audit
idefinaudit = deepcopy(simple_import_data.simpleMeeting)
idefinaudit.id = 'idefin-audit'
idefinaudit.title = "Comité d'Audit"
idefinaudit.shortName = 'IdefinAudit'
idefinaudit.configGroup = 'idefin'
idefinaudit.folderTitle = "Comité d'Audit"
idefinaudit.podTemplates = reuse_templates

# IDEFIN - Rémunération
idefinremun = deepcopy(simple_import_data.simpleMeeting)
idefinremun.id = 'idefin-remun'
idefinremun.title = "Comité de Rémunération"
idefinremun.shortName = 'IdefinRemun'
idefinremun.configGroup = 'idefin'
idefinremun.folderTitle = "Comité de Rémunération"
idefinremun.podTemplates = reuse_templates

# IDEFIN - AG
idefinag = deepcopy(simple_import_data.simpleMeeting)
idefinag.id = 'idefin-ag'
idefinag.title = "Assemblée Générale"
idefinag.shortName = 'IdefinAG'
idefinag.configGroup = 'idefin'
idefinag.folderTitle = "Assemblée Générale"
idefinag.podTemplates = reuse_templates

cfgs = (bepca, bepaudit, bepremun, bepag,
        expaca, expaaudit, exparemun, expaag,
        enviroca, enviroaudit, enviroremun, enviroag,
        cremaca, cremaaudit, cremaremun, cremaag,
        idefinca, idefinaudit, idefinremun, idefinag)

for cfg in cfgs:
    cfg.budgetDefault = '<p>La dépense sera imputée sur le budget n°<span class="highlight-yellow"> XXX</span> ' \
        'dont le solde permet de supporter celle-ci.</p>'
    # assembly and signatures
    cfg.certifiedSignatures = (
        {'function': 'Directeur, Secr\xc3\xa9tariat G\xc3\xa9n\xc3\xa9ral',
         'signatureNumber': '1',
         'date_from': '',
         'name': 'O. GRANVILLE',
         'function': '',
         'date_to': ''},
        {'function': 'Le Signataire 2 FF',
         'signatureNumber': '2',
         'date_from': '',
         'name': 'Vraiment Exemple',
         'function': '',
         'date_to': ''},
        {'function': 'Charg\xc3\xa9 de Mission',
         'signatureNumber': '3',
         'date_from': '',
         'name': 'S. TRIFFOY',
         'function': '',
         'date_to': ''},
        {'function': 'Directeur, Secr\xc3\xa9tariat G\xc3\xa9n\xc3\xa9ral',
         'signatureNumber': '4',
         'date_from': '',
         'name': 'O. GRANVILLE',
         'function': '',
         'date_to': ''})
    # data
    cfg.useGroupsAsCategories = False
    cfg.usedMeetingAttributes = ['startDate', 'endDate', 'attendees', 'excused',
                                 'signatories', 'replacements', 'place', 'observations', ]
    # AG
    if cfg.id.endswith('-ag'):
        cfg.usedMeetingAttributes = ['startDate', 'endDate', 'assembly', 'signatures', 'place', 'observations', ]
    cfg.categories = categories

    # gui
    cfg.itemColumns = (u'item_reference', u'Creator', u'ModificationDate', u'review_state', u'getProposingGroup',
                       u'advices', u'linkedMeetingDate', u'getPreferredMeetingDate', u'actions')
    cfg.meetingColumns = (u'Creator', u'CreationDate', u'review_state', u'actions')
    cfg.itemsListVisibleColumns = (u'item_reference', u'Creator', u'ModificationDate', u'review_state',
                                   u'getProposingGroup', u'advices', u'actions')
    cfg.availableItemsListVisibleColumns = (u'Creator', u'ModificationDate', u'getProposingGroup',
                                            u'advices', u'getPreferredMeetingDate', u'actions')
    cfg.dashboardItemsListingsFilters = (u'c4', u'c5', u'c6', u'c7', u'c8', u'c9', u'c10', u'c11',
                                         u'c13', u'c14', u'c15', u'c17', u'c18', u'c19')
    cfg.dashboardMeetingAvailableItemsFilters = (u'c4', u'c5', u'c7', u'c8', u'c11',
                                                 u'c13', u'c14', u'c17', u'c19')
    cfg.dashboardMeetingLinkedItemsFilters = (u'c4', u'c5', u'c6', u'c7', u'c8',
                                              u'c11', u'c13', u'c14', u'c17', u'c19')
    # workflow
    cfg.workflowAdaptations = (
        u'no_global_observation', u'no_publication',
        u'presented_item_back_to_proposed',  # u'return_to_proposing_group',
        u'accepted_out_of_meeting', u'accepted_out_of_meeting_emergency_and_duplicated', u'refused')
    cfg.itemConditionsInterface = 'Products.MeetingBEP.interfaces.IMeetingItemBEPWorkflowConditions'
    cfg.itemActionsInterface = 'Products.MeetingBEP.interfaces.IMeetingItemBEPWorkflowActions'
    cfg.meetingConditionsInterface = 'Products.MeetingBEP.interfaces.IMeetingBEPWorkflowConditions'
    cfg.meetingActionsInterface = 'Products.MeetingBEP.interfaces.IMeetingBEPWorkflowActions'
    cfg.transitionsToConfirm = (
        u'MeetingItem.accept_but_modify', u'MeetingItem.accept_out_of_meeting_emergency',
        u'MeetingItem.accept_out_of_meeting', u'MeetingItem.pre_accept',
        u'MeetingItem.propose', u'MeetingItem.refuse', u'MeetingItem.backToItemCreated',
        u'MeetingItem.backToProposed', u'MeetingItem.backToValidatedFromAcceptedOutOfMeeting',
        u'MeetingItem.backToValidatedFromAcceptedOutOfMeetingEmergency', u'MeetingItem.delay',
        u'MeetingItem.backToValidated', u'MeetingItem.validate')
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
    cfg.onMeetingTransitionItemTransitionToTrigger = (
        {'meeting_transition': 'freeze', 'item_transition': 'itemfreeze'},
        {'meeting_transition': 'decide', 'item_transition': 'itemfreeze'},
        {'meeting_transition': 'close', 'item_transition': 'itemfreeze'},
        {'meeting_transition': 'close', 'item_transition': 'accept'})
    # advices and access
    cfg.usedAdviceTypes = (u'asked_again', u'positive', u'positive_with_remarks', u'negative', u'nil')
    cfg.enableAdviceConfidentiality = True
    cfg.adviceConfidentialityDefault = True
    cfg.itemPowerObserversStates = (u'accepted', u'accepted_but_modified', u'pre_accepted',
                                    u'itemfrozen', u'refused', u'delayed')
    cfg.meetingPowerObserversStates = (u'closed', u'decided', u'frozen')
    cfg.itemRestrictedPowerObserversStates = (u'accepted', u'accepted_but_modified', u'pre_accepted',
                                              u'itemfrozen', u'refused', u'delayed')
    cfg.meetingRestrictedPowerObserversStates = (u'closed', u'decided', u'frozen')
    cfg.adviceConfidentialFor = ('restricted_power_observers', )
    cfg.hideHistoryTo = ('restricted_power_observers', )
    cfg.itemAdviceStates = ('proposed',)
    cfg.itemAdviceEditStates = ('proposed',)
    cfg.itemAdviceViewStates = (u'accepted', u'accepted_but_modified', u'accepted_out_of_meeting',
                                u'accepted_out_of_meeting_emergency', u'pre_accepted', u'itemfrozen',
                                u'proposed', u'presented', u'refused', u'delayed', u'validated')
    cfg.customAdvisers = (
        {'delay_label': '',
         'for_item_created_until': '',
         'available_on': '',
         'delay': '',
         'gives_auto_advice_on_help_message': '',
         'gives_auto_advice_on': 'python: True',
         'org': 'service-juridique',
         'delay_left_alert': '',
         'is_linked_to_previous_row': '0',
         'for_item_created_from': '2018/01/01',
         'row_id': '2018-12-14.3789235136'},
        {'delay_label': '',
         'for_item_created_until': '',
         'available_on': '',
         'delay': '',
         'gives_auto_advice_on_help_message': '',
         'gives_auto_advice_on': 'python: True',
         'org': 'finances-et-comptabilite',
         'delay_left_alert': '',
         'is_linked_to_previous_row': '0',
         'for_item_created_from': '2018/01/01',
         'row_id': 'row_id_2'},
        {'delay_label': '',
         'for_item_created_until': '',
         'available_on': '',
         'delay': '',
         'gives_auto_advice_on_help_message': '',
         'gives_auto_advice_on': "python: item.getProposingGroup() == pm_utils.org_id_to_uid('coaching-entreprises')",
         'org': 'coaching-entreprises-chef-de-service',
         'delay_left_alert': '',
         'is_linked_to_previous_row': '0',
         'for_item_created_from': '2018/08/01',
         'row_id': 'row_id_1'},
        {'delay_label': '',
         'for_item_created_until': '',
         'available_on': '',
         'delay': '',
         'gives_auto_advice_on_help_message': '',
         'gives_auto_advice_on': "python: item.getProposingGroup() == pm_utils.org_id_to_uid('communication')",
         'org': 'communication-web-chef-de-service',
         'delay_left_alert': '',
         'is_linked_to_previous_row': '0',
         'for_item_created_from': '2018/12/09',
         'row_id': '2018-12-09.4064779048'},
        {'delay_label': '',
         'for_item_created_until': '',
         'available_on': '',
         'delay': '',
         'gives_auto_advice_on_help_message': '',
         'gives_auto_advice_on': "python: item.getProposingGroup() == pm_utils.org_id_to_uid('logistique')",
         'org': 'logistic-recyparcs-chef-de-serivce',
         'delay_left_alert': '',
         'is_linked_to_previous_row': '0',
         'for_item_created_from': '2018/12/09',
         'row_id': '2018-12-09.4064775388'},
        {'delay_label': '',
         'for_item_created_until': '',
         'available_on': '',
         'delay': '',
         'gives_auto_advice_on_help_message': '',
         'gives_auto_advice_on': "python: item.getProposingGroup() == pm_utils.org_id_to_uid('maitrise-douvrages')",
         'org': 'maitrise-douvrage-chef-de-service',
         'delay_left_alert': '',
         'is_linked_to_previous_row': '0',
         'for_item_created_from': '2018/12/09',
         'row_id': '2018-12-09.4064772101'},
        {'delay_label': '',
         'for_item_created_until': '',
         'available_on': '',
         'delay': '',
         'gives_auto_advice_on_help_message': '',
         'gives_auto_advice_on': "python: item.getProposingGroup() == pm_utils.org_id_to_uid('secretariat')",
         'org': 'secretariat-general-chef-de-service',
         'delay_left_alert': '',
         'is_linked_to_previous_row': '0',
         'for_item_created_from': '2018/12/09',
         'row_id': '2018-12-09.4064780584'},
        {'delay_label': '',
         'for_item_created_until': '',
         'available_on': '',
         'delay': '',
         'gives_auto_advice_on_help_message': '',
         'gives_auto_advice_on': "python: item.getProposingGroup() == pm_utils.org_id_to_uid('traitement-industriel')",
         'org': 'traitement-industriel-etudes-de-projets-chef-de-service',
         'delay_left_alert': '',
         'is_linked_to_previous_row': '0',
         'for_item_created_from': '2018/12/09',
         'row_id': '2018-12-09.4064787347'})
    cfg.useCopies = True
    cfg.selectableCopyGroups = (
        u'dirgen_observers', u'dirgen_reviewers',
        u'secretariat_observers', u'secretariat_reviewers',
        u'communication_observers', u'communication_reviewers',
        u'service-juridique_observers', u'service-juridique_reviewers',
        u'finances-et-comptabilite_observers', u'finances-et-comptabilite_reviewers',
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
        u'coaching-entreprises-chef-de-service_reviewers')
    cfg.itemCopyGroupsStates = (
        u'accepted', u'accepted_but_modified', u'accepted_out_of_meeting',
        u'accepted_out_of_meeting_emergency', u'pre_accepted',
        u'itemfrozen', u'refused', u'delayed')
    cfg.powerAdvisersGroups = (u'dirgen', )

data = PloneMeetingConfiguration(
    meetingFolderTitle='Mes séances',
    meetingConfigs=cfgs,
    orgs=[
        dg_org, sg_org, sgcs_org, com_org, comcs_org, jur_org, fin_org, log_org, logcs_org, rhc_org, sr_org,
        info_org, de_org, ce_org, cecs_org, ai_org, ae_org, is_org, env_org, fact_org,
        coll_org, parsc_org, ti_org, tics_org, dt_org, mo_org, mocs_org, infra_org, amt_org, ne_org,
        crema_org, idefin_org])
data.enableUserPreferences = False
data.configGroups = (
    {'row_id': 'bep', 'label': 'BEP'},
    {'row_id': 'expa', 'label': 'EXPA'},
    {'row_id': 'enviro', 'label': 'ENVIRO'},
    {'row_id': 'crema', 'label': 'CREMA'},
    {'row_id': 'idefin', 'label': 'IDEFIN'},
)
data.usersOutsideGroups = [assembly_member]
