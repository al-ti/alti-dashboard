# The name of the panel to be added to HORIZON_CONFIG. Required.
PANEL = 'mypanel'

# The name of the dashboard the PANEL associated with. Required.
PANEL_DASHBOARD = 'identity'

# Python panel class of the PANEL to be added.
ADD_PANEL = 'alti_dashboard.content.mypanel.panel.MyPanel'

#The slug of the panel group the PANEL is associated with. If you want the panel to show up without a panel group, use the panel group “default”.
PANEL_GROUP = 'default'

# A list of applications to be prepended to INSTALLED_APPS
ADD_INSTALLED_APPS = ['alti_dashboard']

# A list of AngularJS modules to be loaded when Angular bootstraps.
ADD_ANGULAR_MODULES = ['horizon.dashboard.identity.alti_dashboard.mypanel']

# Automatically discover static resources in installed apps
AUTO_DISCOVER_STATIC_FILES = True

# A list of js files to be included in the compressed set of files
ADD_JS_FILES = []

# A list of scss files to be included in the compressed set of files
ADD_SCSS_FILES = ['dashboard/identity/alti_dashboard/mypanel/mypanel.scss']

# A list of template-based views to be added to the header
ADD_HEADER_SECTIONS = ['alti_dashboard.content.mypanel.views.HeaderView',]
