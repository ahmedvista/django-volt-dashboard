@REM usage: manage.py graph_models [-h] [--pygraphviz] [--pydot] [--dot] [--json] [--disable-fields] [--disable-abstract-fields] [--group-models]
@REM                               [--all-applications] [--output OUTPUTFILE] [--layout LAYOUT] [--theme THEME] [--verbose-names]
@REM                               [--language LANGUAGE] [--exclude-columns EXCLUDE_COLUMNS] [--exclude-models EXCLUDE_MODELS]
@REM                               [--include-models INCLUDE_MODELS] [--inheritance] [--no-inheritance] [--hide-relations-from-fields]
@REM                               [--relation-fields-only RELATION_FIELDS_ONLY] [--disable-sort-fields] [--hide-edge-labels]
@REM                               [--arrow-shape {box,crow,curve,icurve,diamond,dot,inv,none,normal,tee,vee}] [--color-code-deletions]
@REM                               [--rankdir {TB,BT,LR,RL}] [--version] [-v {0,1,2,3}] [--settings SETTINGS] [--pythonpath PYTHONPATH] [--traceback]  
@REM                               [--no-color] [--force-color] [--skip-checks]
@REM                               [app_label ...]

@REM Creates a GraphViz dot file for the specified app names. You can pass multiple app names and they will all be combined into a single model.       
@REM Output is usually directed to a dot file.

@REM positional arguments:
@REM   app_label

@REM optional arguments:
@REM   -h, --help            show this help message and exit
@REM   --pygraphviz          Output graph data as image using PyGraphViz.
@REM   --pydot               Output graph data as image using PyDot(Plus).
@REM   --dot                 Output graph data as raw DOT (graph description language) text data.
@REM   --json                Output graph data as JSON
@REM   --disable-fields, -d  Do not show the class member fields
@REM   --disable-abstract-fields
@REM                         Do not show the class member fields that were inherited
@REM   --group-models, -g    Group models together respective to their application
@REM   --all-applications, -a
@REM                         Automatically include all applications from INSTALLED_APPS
@REM   --output OUTPUTFILE, -o OUTPUTFILE
@REM                         Render output file. Type of output dependend on file extensions. Use png or jpg to render graph to image.
@REM   --layout LAYOUT, -l LAYOUT
@REM                         Layout to be used by GraphViz for visualization. Layouts: circo dot fdp neato nop nop1 nop2 twopi
@REM   --theme THEME, -t THEME
@REM                         Theme to use. Supplied are 'original' and 'django2018'. You can create your own by creating dot templates in
@REM                         'django_extentions/graph_models/themename/' template directory.
@REM   --verbose-names, -n   Use verbose_name of models and fields
@REM   --language LANGUAGE, -L LANGUAGE
@REM                         Specify language used for verbose_name localization
@REM   --exclude-columns EXCLUDE_COLUMNS, -x EXCLUDE_COLUMNS
@REM                         Exclude specific column(s) from the graph. Can also load exclude list from file.
@REM   --exclude-models EXCLUDE_MODELS, -X EXCLUDE_MODELS
@REM                         Exclude specific model(s) from the graph. Can also load exclude list from file. Wildcards (*) are allowed.
@REM   --include-models INCLUDE_MODELS, -I INCLUDE_MODELS
@REM                         Restrict the graph to specified models. Wildcards (*) are allowed.
@REM   --inheritance, -e     Include inheritance arrows (default)
@REM   --no-inheritance, -E  Do not include inheritance arrows
@REM   --hide-relations-from-fields, -R
@REM                         Do not show relations as fields in the graph.
@REM   --relation-fields-only RELATION_FIELDS_ONLY
@REM                         Only display fields that are relevant for relations
@REM   --disable-sort-fields, -S
@REM                         Do not sort fields
@REM   --hide-edge-labels    Do not show relations labels in the graph.
@REM   --arrow-shape {box,crow,curve,icurve,diamond,dot,inv,none,normal,tee,vee}
@REM                         Arrow shape to use for relations. Default is dot. Available shapes: box, crow, curve, icurve, diamond, dot, inv, none,    
@REM                         normal, tee, vee.
@REM   --color-code-deletions
@REM                         Color the relations according to their on_delete setting, where it it applicable. The colors are: red (CASCADE), orange   
@REM                         (SET_NULL), green (SET_DEFAULT), yellow (SET), blue (PROTECT), grey (DO_NOTHING) and purple (RESTRICT).
@REM   --rankdir {TB,BT,LR,RL}
@REM                         Set direction of graph layout. Supported directions: "TB", "LR", "BT", "RL", corresponding to directed graphs drawn from  
@REM                         top to bottom, from left to right, from bottom to top, and from right to left, respectively. Default is TB.
@REM   --version             Show program's version number and exit.
@REM   -v {0,1,2,3}, --verbosity {0,1,2,3}
@REM                         Verbosity level; 0=minimal output, 1=normal output, 2=verbose output, 3=very verbose output
@REM   --settings SETTINGS   The Python path to a settings module, e.g. "myproject.settings.main". If this isn't provided, the DJANGO_SETTINGS_MODULE  
@REM                         environment variable will be used.
@REM   --pythonpath PYTHONPATH
@REM                         A directory to add to the Python path, e.g. "/home/djangoprojects/myproject".
@REM   --traceback           Raise on CommandError exceptions.
@REM   --no-color            Don't colorize the command output.
@REM   --force-color         Force colorization of the command output.
@REM   --skip-checks         Skip system checks.

@echo off

"env\Scripts\python.exe" manage.py graph_models --pydot ^
 --all-applications ^
 --group-models ^
 --color-code-deletions ^
 --arrow-shape normal ^
 --rankdir LR ^
 --theme django2018 ^
 --exclude-models LogEntry,Token,TokenProxy,AbstractBaseSession,Session,AbstractUser,Group,Permission,AbstractBaseUser,PermissionsMixin,ContentType ^
 --output erd.png ^
 
@REM  --verbose-names ^

exit