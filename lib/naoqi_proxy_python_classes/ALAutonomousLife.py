#!/usr/bin/env python
# Class autogenerated from .\alautonomouslifeproxy.h
# by Sammy Pfeiffer's <Sammy.Pfeiffer at student.uts.edu.au> generator
# You need an ALBroker running





class ALAutonomousLife(object):
    def __init__(self, session):
        self.session = session
        self.proxy = None

    def force_connect(self):
        self.proxy = self.session.service("ALAutonomousLife")

    def focusedActivity(self):
        """Returns the currently focused activity

        :returns str: The name of the focused activity
        """
        if not self.proxy:
            self.proxy = self.session.service("ALAutonomousLife")
        return self.proxy.focusedActivity()

    def getActivityNature(self, activity_name):
        """Returns the nature of an activity

        :param str activity_name: The package_name/activity_name to check
        :returns str: Possible values are: solitary, interactive
        """
        if not self.proxy:
            self.proxy = self.session.service("ALAutonomousLife")
        return self.proxy.getActivityNature(activity_name)

    def getActivityStatistics(self):
        """Get launch count, last completion time, etc for activities.

        :returns std::map<std::string , std::map<std::string , int> >: A map of activity names, with a cooresponding map of  "prevStartTime", "prevCompletionTime", "startCount", "totalDuration". Times are 0 for unlaunched Activities
        """
        if not self.proxy:
            self.proxy = self.session.service("ALAutonomousLife")
        return self.proxy.getActivityStatistics()

    def getAutonomousActivityStatistics(self):
        """Get launch count, last completion time, etc for activities with autonomous launch trigger conditions.

        :returns std::map<std::string , std::map<std::string , int> >: A map of activity names, with a cooresponding map of  "prevStartTime", "prevCompletionTime", "startCount", "totalDuration". Times are 0 for unlaunched Activities
        """
        if not self.proxy:
            self.proxy = self.session.service("ALAutonomousLife")
        return self.proxy.getAutonomousActivityStatistics()

    def getEnabledLaunchpadPlugins(self):
        """Get a list of enabled AutonomousLaunchpad Plugins.  Enabled plugins will run when AutonomousLaunchpad is started

        :returns std::vector<std::string>: A list of strings of enabled plugins.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALAutonomousLife")
        return self.proxy.getEnabledLaunchpadPlugins()

    def getFocusHistory(self):
        """Get a list of the order that activities that have been focused, and their time focused.

        :returns std::vector<std::pair<std::string , int> >: A list of pairs, each pair is ActivityName/PreviousFocusedTime
        """
        if not self.proxy:
            self.proxy = self.session.service("ALAutonomousLife")
        return self.proxy.getFocusHistory()

    def getFocusHistory2(self, depth):
        """Get a list of the order that activities that have been focused, and their time focused.

        :param int depth: How many items of history to report, starting from most recent.
        :returns std::vector<std::pair<std::string , int> >: A list of pairs, each pair is ActivityName/PreviousFocusedTime
        """
        if not self.proxy:
            self.proxy = self.session.service("ALAutonomousLife")
        return self.proxy.getFocusHistory(depth)

    def getLaunchpadPluginsForGroup(self, group):
        """Get a list of AutonomousLaunchpad Plugins that belong to specified group

        :param str group: The group to search for the plugins
        :returns std::vector<std::string>: A list of strings of the plugins belonging to the group.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALAutonomousLife")
        return self.proxy.getLaunchpadPluginsForGroup(group)

    def setAutonomousAbilityEnabled(self, value):
        if not self.proxy:
            self.proxy = self.session.service("ALAutonomousLife")
        return self.proxy.setAutonomousAbilityEnabled("BasicAwareness", value)

    def getLifeTime(self):
        """Get the time in seconds as life sees it.  Based on gettimeofday()

        :returns int: The int time in seconds as Autonomous Life sees it
        """
        if not self.proxy:
            self.proxy = self.session.service("ALAutonomousLife")
        return self.proxy.getLifeTime()

    def getRobotOffsetFromFloor(self):
        """Get the vertical offset (in meters) of the base of the robot with respect to the floor

        :returns float: Current vertical offset (in meters)
        """
        if not self.proxy:
            self.proxy = self.session.service("ALAutonomousLife")
        return self.proxy.getRobotOffsetFromFloor()

    def getState(self):
        """Returns the current state of AutonomousLife

        :returns str: Can be: solitary, interactive, safeguard, disabled
        """
        if not self.proxy:
            self.proxy = self.session.service("ALAutonomousLife")
        return self.proxy.getState()

    def getStateHistory(self, depth):
        """Get a list of the order that states that have been entered, and their time entered.

        :param int depth: How many items of history to report, starting from most recent.
        :returns std::vector<std::pair<std::string , int> >: A list of pairs, each pair is StateName/PreviousEnteredTime
        """
        if not self.proxy:
            self.proxy = self.session.service("ALAutonomousLife")
        return self.proxy.getStateHistory(depth)

    def getStateHistory2(self):
        """Get a list of the order that states that have been entered, and their time entered.

        :returns std::vector<std::pair<std::string , int> >: A list of pairs, each pair is StateName/PreviousEnteredTime
        """
        if not self.proxy:
            self.proxy = self.session.service("ALAutonomousLife")
        return self.proxy.getStateHistory()

    def isMonitoringLaunchpadConditions(self):
        """Gets running status of AutonomousLaunchpad

        :returns bool: True if AutonomousLaunchpad is monitoring ALMemory and reporting conditional triggers.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALAutonomousLife")
        return self.proxy.isMonitoringLaunchpadConditions()

    def isSafeguardEnabled(self, name):
        """Get if a given safeguard will be handled by Autonomous Life or not.

        :param str name: Name of the safeguard to consider: RobotPushed, RobotFell,CriticalDiagnosis, CriticalTemperature
        :returns bool: True if life handles the safeguard.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALAutonomousLife")
        return self.proxy.isSafeguardEnabled(name)

    def ping(self):
        """Just a ping. Always returns true

        :returns bool: returns true
        """
        if not self.proxy:
            self.proxy = self.session.service("ALAutonomousLife")
        return self.proxy.ping()

    def preloadActivities(self):
        """Preload activities to optimize launching
        """
        if not self.proxy:
            self.proxy = self.session.service("ALAutonomousLife")
        return self.proxy.preloadActivities()

    def setLaunchpadPluginEnabled(self, plugin_name, enabled):
        """Temporarily enables/disables AutonomousLaunchpad Plugins

        :param str plugin_name: The name of the plugin to enable/disable
        :param bool enabled: Whether or not to enable this plugin
        """
        if not self.proxy:
            self.proxy = self.session.service("ALAutonomousLife")
        return self.proxy.setLaunchpadPluginEnabled(plugin_name, enabled)

    def setRobotOffsetFromFloor(self, offset):
        """Set the vertical offset (in meters) of the base of the robot with respect to the floor

        :param float offset: The new vertical offset (in meters)
        """
        if not self.proxy:
            self.proxy = self.session.service("ALAutonomousLife")
        return self.proxy.setRobotOffsetFromFloor(offset)

    def setSafeguardEnabled(self, name, enabled):
        """Set if a given safeguard will be handled by Autonomous Life or not.

        :param str name: Name of the safeguard to consider: RobotPushed, RobotFell,CriticalDiagnosis, CriticalTemperature
        :param bool enabled: True if life handles the safeguard.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALAutonomousLife")
        return self.proxy.setSafeguardEnabled(name, enabled)

    def setState(self, state):
        """Programatically control the state of Autonomous Life

        :param str state: The possible states of AutonomousLife are: interactive, solitary, safeguard, disabled
        """
        if not self.proxy:
            self.proxy = self.session.service("ALAutonomousLife")
        return self.proxy.setState(state)

    def startMonitoringLaunchpadConditions(self):
        """Start monitoring ALMemory and reporting conditional triggers with AutonomousLaunchpad.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALAutonomousLife")
        return self.proxy.startMonitoringLaunchpadConditions()

    def stopAll(self):
        """Stops the focused activity and clears stack of activities
        """
        if not self.proxy:
            self.proxy = self.session.service("ALAutonomousLife")
        return self.proxy.stopAll()

    def stopFocus(self):
        """Stops the focused activity. If another activity is stacked it will be started.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALAutonomousLife")
        return self.proxy.stopFocus()

    def stopMonitoringLaunchpadConditions(self):
        """Stop monitoring ALMemory and reporting conditional triggers with AutonomousLaunchpad.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALAutonomousLife")
        return self.proxy.stopMonitoringLaunchpadConditions()

    def switchFocus(self, activity_name, flags):
        """Set an activity as running with user focus

        :param str activity_name: The package_name/activity_name to run
        :param int flags: Flags for focus changing. STOP_CURRENT or STOP_AND_STACK_CURRENT
        """
        if not self.proxy:
            self.proxy = self.session.service("ALAutonomousLife")
        return self.proxy.switchFocus(activity_name, flags)

    def switchFocus2(self, activity_name):
        """Set an activity as running with user focus

        :param str activity_name: The package_name/activity_name to run
        """
        if not self.proxy:
            self.proxy = self.session.service("ALAutonomousLife")
        return self.proxy.switchFocus(activity_name)

    def version(self):
        """Returns the version of the module.

        :returns str: A string containing the version of the module.
        """
        if not self.proxy:
            self.proxy = self.session.service("ALAutonomousLife")
        return self.proxy.version()
