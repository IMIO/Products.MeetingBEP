Changelog
=========

4.1b3 (unreleased)
------------------

- Adapted call to ToolPloneMeeting.isPowerObserverForCfg now that parameter
  isRestricted=True is replaced by power_observer_type='restrictedpowerobservers'.
- Use PloneMeetingTestCase._setPowerObserverStates to define power observers states.

4.1b2 (2019-01-31)
------------------

- Configure profile

4.1b1 (2018-12-04)
------------------

- Restricted power observers have... restricted access to some informations of
  the item, no access to :
  - history (of every content, item, meeting, advice);
  - item observations.
- Items are not privacyViewable by restricted power observers when :
  - using HR confidential proposing group;
  - item is returned to proposing group for corrections.
- When an item is accepted_out_of_meeting_emergency, the decision of duplicated
  item is automatically adapted to manage "ratification".
- Hide field 'Observations' on advice using CSS.
- Override message 'No access' with something smoother.