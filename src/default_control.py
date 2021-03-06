"""
G'DAY default control flags

Read into the model unless the user changes these at runtime with definitions
in the .INI file

"""

__author__  = "Martin De Kauwe"
__version__ = "1.0 (05.09.2011)"
__email__   = "mdekauwe@gmail.com"

water_model = 1        # Water balance model
assim_model = 7        # 0-4=McM, 5+6=Bewdy, 7=mate
nuptake_model = 1      # 0=constant uptake, 1=func of N inorgn, 2=depends on rate of soil N availability
trans_model = 1        # 0=trans from WUE, 1=Penman-Monteith, 2=Priestley-Taylor
fixroot = 0            #
fixleafnc = 0          # fixed leaf N C ?
leuning_func = 0       #
passiveconst = 0       # hold passive pool at passivesoil
print_options = 1      # 0=every timestep, 1=end of run
grazing = 0            # Is foliage grazed 0=No, 1=Yes
use_eff_nc = 0         # use constant leaf n:c for  metfrac s
strfloat = 0           # Structural pool input N:C varies=1, fixed=0
use_leuning = 0
co2_conc = 0           # 0=ambient, 1=elevated
fixed_stem_nc = 1      # 0=vary stem N:C with foliage, 1=fixed stem N:C
deciduous_model = 0    # evergreen_model=0, deciduous_model=1
calc_sw_params = 0     # 0=user supplies field capacity and wilting point, 1=calculate them based on cosby et al.
water_stress = 1       # water stress modifier turned on=1 (default)...ability to turn off to test things without drought stress = 0
modeljm = 1            # modeljm=0, Jmax and Vcmax parameters are read in, modeljm=1, parameters are calculated from leaf N content
model_optroot = 0      # Ross's optimal root model...not sure if this works yet...0=off, 1=on