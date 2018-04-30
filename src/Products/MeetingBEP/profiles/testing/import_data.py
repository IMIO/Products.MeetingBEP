# -*- coding: utf-8 -*-
from Products.PloneMeeting.profiles import AnnexTypeDescriptor
from Products.PloneMeeting.profiles import CategoryDescriptor
from Products.PloneMeeting.profiles import GroupDescriptor
from Products.PloneMeeting.profiles import ItemAnnexSubTypeDescriptor
from Products.PloneMeeting.profiles import ItemAnnexTypeDescriptor
from Products.PloneMeeting.profiles import ItemTemplateDescriptor
from Products.PloneMeeting.profiles import MeetingConfigDescriptor
from Products.PloneMeeting.profiles import MeetingUserDescriptor
from Products.PloneMeeting.profiles import PloneGroupDescriptor
from Products.PloneMeeting.profiles import PloneMeetingConfiguration
from Products.PloneMeeting.profiles import PodTemplateDescriptor
from Products.PloneMeeting.profiles import RecurringItemDescriptor
from Products.PloneMeeting.profiles import UserDescriptor


# Annex types
overheadAnalysisSubtype = ItemAnnexSubTypeDescriptor(
    'overhead-analysis-sub-annex',
    'Overhead analysis sub annex',
    other_mc_correspondences=(
        'codir_-_annexes_types_-_item_annexes_-_budget-analysis', ))

overheadAnalysis = ItemAnnexTypeDescriptor(
    'overhead-analysis', 'Administrative overhead analysis',
    u'overheadAnalysis.png',
    subTypes=[overheadAnalysisSubtype],
    other_mc_correspondences=(
        'codir_-_annexes_types_-_item_annexes_-_budget-analysis_-_budget-analysis-sub-annex', ))

financialAnalysisSubAnnex = ItemAnnexSubTypeDescriptor(
    'financial-analysis-sub-annex',
    'Financial analysis sub annex')

financialAnalysis = ItemAnnexTypeDescriptor(
    'financial-analysis', 'Financial analysis', u'financialAnalysis.png',
    u'Predefined title for financial analysis', subTypes=[financialAnalysisSubAnnex])

legalAnalysis = ItemAnnexTypeDescriptor(
    'legal-analysis', 'Legal analysis', u'legalAnalysis.png')

budgetAnalysisCfg2Subtype = ItemAnnexSubTypeDescriptor(
    'budget-analysis-sub-annex',
    'Budget analysis sub annex')

budgetAnalysisCfg2 = ItemAnnexTypeDescriptor(
    'budget-analysis', 'Budget analysis', u'budgetAnalysis.png',
    subTypes=[budgetAnalysisCfg2Subtype])

budgetAnalysisCfg1Subtype = ItemAnnexSubTypeDescriptor(
    'budget-analysis-sub-annex',
    'Budget analysis sub annex',
    other_mc_correspondences=(
        'codir_-_annexes_types_-_item_annexes_-_budget-analysis_-_budget-analysis-sub-annex', ))

budgetAnalysisCfg1 = ItemAnnexTypeDescriptor(
    'budget-analysis', 'Budget analysis', u'budgetAnalysis.png',
    subTypes=[budgetAnalysisCfg1Subtype],
    other_mc_correspondences=('codir_-_annexes_types_-_item_annexes_-_budget-analysis', ))

itemAnnex = ItemAnnexTypeDescriptor(
    'item-annex', 'Other annex(es)', u'itemAnnex.png')
# Could be used once we
# will digitally sign decisions ? Indeed, once signed, we will need to
# store them (together with the signature) as separate files.
decision = ItemAnnexTypeDescriptor(
    'decision', 'Decision', u'decision.png', relatedTo='item_decision')
decisionAnnex = ItemAnnexTypeDescriptor(
    'decision-annex', 'Decision annex(es)', u'decisionAnnex.png', relatedTo='item_decision')
# A vintage annex type
marketingAnalysis = ItemAnnexTypeDescriptor(
    'marketing-annex', 'Marketing annex(es)', u'legalAnalysis.png', relatedTo='item_decision',
    enabled=False)
# Advice annex types
adviceAnnex = AnnexTypeDescriptor(
    'advice-annex', 'Advice annex(es)', u'itemAnnex.png', relatedTo='advice')
adviceLegalAnalysis = AnnexTypeDescriptor(
    'advice-legal-analysis', 'Advice legal analysis', u'legalAnalysis.png', relatedTo='advice')
# Meeting annex types
meetingAnnex = AnnexTypeDescriptor(
    'meeting-annex', 'Meeting annex(es)', u'itemAnnex.png', relatedTo='meeting')

# Pod templates ----------------------------------------------------------------
agendaTemplate = PodTemplateDescriptor('agendaTemplate', 'Meeting agenda')
agendaTemplate.odt_file = 'Agenda.odt'
agendaTemplate.pod_portal_types = ['MeetingCA']
agendaTemplate.tal_condition = ''

decisionsTemplate = PodTemplateDescriptor('decisionsTemplate',
                                          'Meeting decisions')
decisionsTemplate.odt_file = 'Decisions.odt'
decisionsTemplate.pod_portal_types = ['MeetingCA']
decisionsTemplate.tal_condition = 'python:here.adapted().isDecided()'

itemTemplate = PodTemplateDescriptor('itemTemplate', 'Meeting item')
itemTemplate.odt_file = 'Item.odt'
itemTemplate.pod_portal_types = ['MeetingItemCA']
itemTemplate.tal_condition = ''

# item templates
template1 = ItemTemplateDescriptor(id='template1',
                                   title='Tutelle CPAS',
                                   description='<p>Tutelle CPAS</p>',
                                   category='',
                                   proposingGroup='developers',
                                   templateUsingGroups=['developers', 'vendors'],
                                   decision=""" """)
template2 = ItemTemplateDescriptor(id='template2',
                                   title='Contrôle médical systématique agent contractuel',
                                   description='<p>Contrôle médical systématique agent contractuel</p>',
                                   category='',
                                   proposingGroup='vendors',
                                   templateUsingGroups=['vendors', ],
                                   decision=""" """)


# Categories -------------------------------------------------------------------
deployment = CategoryDescriptor('deployment', 'Deployment topics')
maintenance = CategoryDescriptor('maintenance', 'Maintenance topics')
development = CategoryDescriptor('development', 'Development topics')
events = CategoryDescriptor('events', 'Events')
research = CategoryDescriptor('research', 'Research topics')
projects = CategoryDescriptor('projects', 'Projects')
# A vintage category
marketing = CategoryDescriptor('marketing', 'Marketing', active=False)
# usingGroups category
subproducts = CategoryDescriptor('subproducts', 'Subproducts wishes', usingGroups=('vendors',))

# Classifiers
classifier1 = CategoryDescriptor('classifier1', 'Classifier 1')
classifier2 = CategoryDescriptor('classifier2', 'Classifier 2')
classifier3 = CategoryDescriptor('classifier3', 'Classifier 3')

# Users and groups -------------------------------------------------------------
pmManager = UserDescriptor('pmManager', [], email="pmmanager@plonemeeting.org", fullname='M. PMManager')
pmCreator1 = UserDescriptor('pmCreator1', [], email="pmcreator1@plonemeeting.org", fullname='M. PMCreator One')
pmCreator1b = UserDescriptor('pmCreator1b', [], email="pmcreator1b@plonemeeting.org", fullname='M. PMCreator One bee')
pmObserver1 = UserDescriptor('pmObserver1', [], email="pmobserver1@plonemeeting.org", fullname='M. PMObserver One')
pmReviewer1 = UserDescriptor('pmReviewer1', [])
pmReviewerLevel1 = UserDescriptor('pmReviewerLevel1', [],
                                  email="pmreviewerlevel1@plonemeeting.org", fullname='M. PMReviewer Level One')
pmCreator2 = UserDescriptor('pmCreator2', [])
pmReviewer2 = UserDescriptor('pmReviewer2', [])
pmReviewerLevel2 = UserDescriptor('pmReviewerLevel2', [],
                                  email="pmreviewerlevel2@plonemeeting.org", fullname='M. PMReviewer Level Two')
pmAdviser1 = UserDescriptor('pmAdviser1', [])
voter1 = UserDescriptor('voter1', [], fullname='M. Voter One')
voter2 = UserDescriptor('voter2', [], fullname='M. Voter Two')
powerobserver1 = UserDescriptor('powerobserver1',
                                [],
                                email="powerobserver1@plonemeeting.org",
                                fullname='M. Power Observer1')
# powerobserver1 is 'power observer' because in the ca '_powerobservers' group
ca_powerobservers = PloneGroupDescriptor('ca_powerobservers',
                                         'ca_powerobservers',
                                         [])
powerobserver1.ploneGroups = [ca_powerobservers, ]
powerobserver2 = UserDescriptor('powerobserver2',
                                [],
                                email="powerobserver2@plonemeeting.org",
                                fullname='M. Power Observer2')
restrictedpowerobserver1 = UserDescriptor('restrictedpowerobserver1',
                                          [],
                                          email="restrictedpowerobserver1@plonemeeting.org",
                                          fullname='M. Restricted Power Observer 1')
ca_restrictedpowerobservers = PloneGroupDescriptor('ca_restrictedpowerobservers',
                                                   'ca_restrictedpowerobservers',
                                                   [])
restrictedpowerobserver1.ploneGroups = [ca_restrictedpowerobservers, ]
restrictedpowerobserver2 = UserDescriptor('restrictedpowerobserver2',
                                          [],
                                          email="restrictedpowerobserver2@plonemeeting.org",
                                          fullname='M. Restricted Power Observer 2')
codir_restrictedpowerobservers = PloneGroupDescriptor('codir_restrictedpowerobservers',
                                                      'codir_restrictedpowerobservers',
                                                      [])
restrictedpowerobserver2.ploneGroups = [codir_restrictedpowerobservers, ]

developers = GroupDescriptor('developers', 'Developers', 'Devel')
developers.creators.append(pmCreator1)
developers.creators.append(pmCreator1b)
developers.creators.append(pmManager)
developers.prereviewers.append(pmReviewerLevel1)
developers.reviewers.append(pmReviewer1)
developers.reviewers.append(pmManager)
developers.reviewers.append(pmReviewerLevel2)
developers.observers.append(pmObserver1)
developers.observers.append(pmReviewer1)
developers.observers.append(pmManager)
developers.advisers.append(pmAdviser1)
developers.advisers.append(pmManager)
setattr(developers, 'signatures', 'developers signatures')
setattr(developers, 'echevinServices', 'developers')

# give an advice on recurring items
vendors = GroupDescriptor('vendors', 'Vendors', 'Devil')
vendors.creators.append(pmCreator2)
vendors.reviewers.append(pmReviewer2)
vendors.observers.append(pmReviewer2)
vendors.advisers.append(pmReviewer2)
vendors.advisers.append(pmManager)
setattr(vendors, 'signatures', '')

# Do voters able to see items to vote for
developers.observers.append(voter1)
developers.observers.append(voter2)
vendors.observers.append(voter1)
vendors.observers.append(voter2)

# Add a vintage group
endUsers = GroupDescriptor('endUsers', 'End users', 'EndUsers', active=False)

pmManager_observer = MeetingUserDescriptor('pmManager',
                                           duty='Secrétaire de la Chancellerie',
                                           usages=['assemblyMember'])
cadranel_signer = MeetingUserDescriptor('cadranel', duty='Secrétaire',
                                        usages=['assemblyMember', 'signer'],
                                        signatureImage='SignatureCadranel.jpg',
                                        signatureIsDefault=True)
# Add meeting users (voting purposes)
muser_voter1 = MeetingUserDescriptor('voter1', duty='Voter1',
                                     usages=['assemblyMember', 'voter', ])
muser_voter2 = MeetingUserDescriptor('voter2', duty='Voter2',
                                     usages=['assemblyMember', 'voter', ])

# budget impact editors
budgetimpacteditor = UserDescriptor('budgetimpacteditor',
                                    [],
                                    email="budgetimpacteditor@plonemeeting.org",
                                    fullname='M. Budget Impact Editor')
ca_budgetimpacteditors = PloneGroupDescriptor('ca_budgetimpacteditors',
                                              'ca_budgetimpacteditors',
                                              [])
budgetimpacteditor.ploneGroups = [ca_budgetimpacteditors,
                                  ca_powerobservers]

# Meeting configurations -------------------------------------------------------
# CA
ca = MeetingConfigDescriptor(
    'ca', 'CA', 'CA', isDefault=True)
ca.meetingManagers = ['pmManager', ]
ca.assembly = 'Pierre Dupont - Bourgmestre,\n' \
               'Charles Exemple - 1er Echevin,\n' \
               'Echevin Un, Echevin Deux, Echevin Trois - Echevins,\n' \
               'Jacqueline Exemple, Responsable du CPAS'
ca.signatures = 'Pierre Dupont, Bourgmestre - Charles Exemple, Secrétaire communal'
ca.certifiedSignatures = []
ca.categories = [development, research, events]
ca.classifiers = [classifier1, classifier2, classifier3]
ca.shortName = 'CA'
ca.annexTypes = [financialAnalysis, budgetAnalysisCfg1, overheadAnalysis,
                 itemAnnex, decisionAnnex, marketingAnalysis,
                 adviceAnnex, adviceLegalAnalysis, meetingAnnex]
ca.usedItemAttributes = ('toDiscuss', 'associatedGroups', 'itemIsSigned',)
ca.maxShownListings = '100'
ca.itemWorkflow = 'meetingitemcommunes_workflow'
ca.meetingWorkflow = 'meetingcommunes_workflow'
ca.itemConditionsInterface = 'Products.MeetingBEP.interfaces.IMeetingItemBEPWorkflowConditions'
ca.itemActionsInterface = 'Products.MeetingBEP.interfaces.IMeetingItemBEPWorkflowActions'
ca.meetingConditionsInterface = 'Products.MeetingBEP.interfaces.IMeetingBEPWorkflowConditions'
ca.meetingActionsInterface = 'Products.MeetingBEP.interfaces.IMeetingBEPWorkflowActions'
ca.transitionsToConfirm = []
ca.transitionsForPresentingAnItem = ['propose', 'validate', 'present', ]
ca.onMeetingTransitionItemTransitionToTrigger = ({'meeting_transition': 'freeze',
                                                  'item_transition': 'itemfreeze'},
                                                 {'meeting_transition': 'decide',
                                                  'item_transition': 'itemfreeze'},
                                                 {'meeting_transition': 'publish_decisions',
                                                  'item_transition': 'itemfreeze'},
                                                 {'meeting_transition': 'publish_decisions',
                                                  'item_transition': 'accept'},
                                                 {'meeting_transition': 'close',
                                                  'item_transition': 'itemfreeze'},
                                                 {'meeting_transition': 'close',
                                                  'item_transition': 'accept'},
                                                 {'meeting_transition': 'backToCreated',
                                                  'item_transition': 'backToPresented'},)

ca.meetingTopicStates = ('created', 'frozen')
ca.decisionTopicStates = ('decided', 'closed')
ca.useAdvices = True
ca.selectableAdvisers = ['developers', 'vendors']
ca.itemAdviceStates = ['proposed', ]
ca.itemAdviceEditStates = ['proposed', 'validated']
ca.itemAdviceViewStates = ['presented', ]
ca.transitionsReinitializingDelays = ('backToItemCreated', )
ca.enforceAdviceMandatoriness = False
ca.itemPowerObserversStates = ('itemcreated', 'presented', 'accepted', 'delayed')
ca.itemDecidedStates = ['accepted', 'delayed', 'accepted_but_modified', 'pre_accepted']
ca.workflowAdaptations = ['no_publication', 'no_global_observation']
ca.insertingMethodsOnAddItem = ({'insertingMethod': 'on_proposing_groups',
                                 'reverse': '0'}, )
ca.useGroupsAsCategories = True
ca.meetingPowerObserversStates = ('frozen', 'decided', 'closed')
ca.useCopies = True
ca.selectableCopyGroups = [developers.getIdSuffixed('reviewers'), vendors.getIdSuffixed('reviewers'), ]
ca.podTemplates = [agendaTemplate, decisionsTemplate, itemTemplate]
ca.meetingConfigsToCloneTo = [{'meeting_config': 'codir',
                               'trigger_workflow_transitions_until': '__nothing__'}, ]
ca.itemAutoSentToOtherMCStates = ('accepted', 'accepted_but_modified', )
ca.recurringItems = [
    RecurringItemDescriptor(
        id='recItem1',
        description='<p>This is the first recurring item.</p>',
        title='Recurring item #1',
        proposingGroup='developers',
        decision='First recurring item approved'),

    RecurringItemDescriptor(
        id='recItem2',
        title='Recurring item #2',
        description='<p>This is the second recurring item.</p>',
        proposingGroup='developers',
        decision='Second recurring item approved'),
]
ca.itemTemplates = (template1, template2)

# CoDir
codir = MeetingConfigDescriptor(
    'codir', 'CoDir',
    'CoDir')
codir.meetingManagers = ['pmManager', ]
codir.assembly = 'Default assembly'
codir.signatures = 'Default signatures'
codir.certifiedSignatures = []
codir.categories = [deployment, maintenance, development, events,
                    research, projects, marketing, subproducts]
codir.classifiers = [classifier1, classifier2, classifier3]
codir.shortName = 'CoDir'
codir.annexTypes = [financialAnalysis, legalAnalysis, budgetAnalysisCfg2, itemAnnex,
                    decisionAnnex, adviceAnnex, adviceLegalAnalysis, meetingAnnex]
codir.itemWorkflow = 'meetingitemcommunes_workflow'
codir.meetingWorkflow = 'meetingcommunes_workflow'
codir.itemConditionsInterface = 'Products.MeetingBEP.interfaces.IMeetingItemBEPWorkflowConditions'
codir.itemActionsInterface = 'Products.MeetingBEP.interfaces.IMeetingItemBEPWorkflowActions'
codir.meetingConditionsInterface = 'Products.MeetingBEP.interfaces.IMeetingBEPWorkflowConditions'
codir.meetingActionsInterface = 'Products.MeetingBEP.interfaces.IMeetingBEPWorkflowActions'
codir.transitionsToConfirm = []
codir.transitionsForPresentingAnItem = ['propose', 'validate', 'present', ]
codir.onMeetingTransitionItemTransitionToTrigger = ({'meeting_transition': 'freeze',
                                                     'item_transition': 'itemfreeze'},
                                                    {'meeting_transition': 'publish',
                                                     'item_transition': 'itemfreeze'},
                                                    {'meeting_transition': 'publish',
                                                     'item_transition': 'itempublish'},
                                                    {'meeting_transition': 'decide',
                                                     'item_transition': 'itemfreeze'},
                                                    {'meeting_transition': 'decide',
                                                     'item_transition': 'itempublish'},
                                                    {'meeting_transition': 'publish_decisions',
                                                     'item_transition': 'itemfreeze'},
                                                    {'meeting_transition': 'publish_decisions',
                                                     'item_transition': 'itempublish'},
                                                    {'meeting_transition': 'publish_decisions',
                                                     'item_transition': 'accept'},
                                                    {'meeting_transition': 'close',
                                                     'item_transition': 'itemfreeze'},
                                                    {'meeting_transition': 'close',
                                                     'item_transition': 'itempublish'},
                                                    {'meeting_transition': 'close',
                                                     'item_transition': 'accept'},
                                                    {'meeting_transition': 'backToCreated',
                                                     'item_transition': 'backToPresented'},)

codir.meetingTopicStates = ('created', 'frozen', 'published')
codir.decisionTopicStates = ('decided', 'closed')
codir.itemAdviceStates = ('validated',)
codir.usedItemAttributes = ('toDiscuss', 'associatedGroups', 'itemIsSigned',)
codir.insertingMethodsOnAddItem = ({'insertingMethod': 'on_categories',
                                    'reverse': '0'}, )
codir.useGroupsAsCategories = False
codir.useAdvices = False
codir.selectableAdvisers = []
codir.itemAdviceStates = ['proposed', ]
codir.itemAdviceEditStates = ['proposed', 'validated']
codir.itemAdviceViewStates = ['presented', ]
codir.transitionsReinitializingDelays = 'backToItemCreated'
codir.enforceAdviceMandatoriness = False
codir.itemDecidedStates = ['accepted', 'delayed', 'accepted_but_modified', 'pre_accepted']
codir.itemPowerObserversStates = ca.itemPowerObserversStates
codir.meetingPowerObserversStates = ca.meetingPowerObserversStates
codir.useCopies = True
codir.selectableCopyGroups = [developers.getIdSuffixed('reviewers'),
                              vendors.getIdSuffixed('reviewers'), ]
codir.useVotes = True
codir.meetingUsers = [muser_voter1, muser_voter2, ]
codir.recurringItems = []
codir.itemTemplates = (template1, template2)

# no recurring items for this meetingConfig, only for tests !!!
# so we can test a meetingConfig with recurring items (ca) and without (codir)

data = PloneMeetingConfiguration(
    meetingFolderTitle='Mes seances',
    meetingConfigs=(ca, codir),
    groups=(developers, vendors, endUsers))
# necessary for testSetup.test_pm_ToolAttributesAreOnlySetOnFirstImportData
data.restrictUsers = False
data.usersOutsideGroups = [voter1, voter2, powerobserver1, powerobserver2,
                           restrictedpowerobserver1, restrictedpowerobserver2,
                           budgetimpacteditor]
# ------------------------------------------------------------------------------
