# Makefile created by mkmf $Id: mkmf,v 1.1.2.1 2009/12/17 00:41:15 nnz Exp $ 

include /home/wenchang/scratch/tiger3/MOM4.1/bin/mkmf.template.tiger3_intelmpi_24

SRCROOT = /home/wenchang/scratch/tiger3/MOM4.1/src/

CPPDEFS = -Duse_netCDF -Duse_netCDF3 -Duse_libMPI -DUSE_OCEAN_BGC -DSPMD -DLAND_BND_TRACERS

.DEFAULT:
	-echo $@ does not exist.
all: fms_CM2.1p1_dynamic.x
FMS_coupler_util.o: /home/wenchang/scratch/tiger3/MOM4.1/src/ocean_shared/generic_tracers/FMS_coupler_util.F90 mpp.o coupler_types.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	/home/wenchang/scratch/tiger3/MOM4.1/src/ocean_shared/generic_tracers/FMS_coupler_util.F90
FMS_ocmip2_co2calc.o: /home/wenchang/scratch/tiger3/MOM4.1/src/ocean_shared/generic_tracers/FMS_ocmip2_co2calc.F90
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	/home/wenchang/scratch/tiger3/MOM4.1/src/ocean_shared/generic_tracers/FMS_ocmip2_co2calc.F90
MISR_simulator.o: $(SRCROOT)atmos_param/cosp/MISR_simulator/MISR_simulator.f
	$(FC) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/cosp/MISR_simulator/MISR_simulator.f
MersenneTwister.o: $(SRCROOT)shared/random_numbers/MersenneTwister.F90
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)shared/random_numbers/MersenneTwister.F90
adv_center.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/adv_center.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/cppdefs.h                                                                  \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/version.h util.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/adv_center.F90
aer_ccn_act.o: $(SRCROOT)atmos_shared/tracer_driver/aer_ccn_act/aer_ccn_act.F90 fms.o mpp.o aer_ccn_act_k.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_shared/tracer_driver/aer_ccn_act/aer_ccn_act.F90
aer_ccn_act_k.o: $(SRCROOT)atmos_shared/tracer_driver/aer_ccn_act/aer_ccn_act_k.F90
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_shared/tracer_driver/aer_ccn_act/aer_ccn_act_k.F90
aer_in_act.o: $(SRCROOT)atmos_shared/tracer_driver/aer_ccn_act/aer_in_act.F90
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_shared/tracer_driver/aer_ccn_act/aer_in_act.F90
aerosol.o: $(SRCROOT)atmos_param/sea_esf_rad/aerosol.F90 time_manager.o diag_manager.o field_manager.o tracer_manager.o fms.o interpolator.o mpp_io.o constants.o rad_utilities.o mpp.o mpp_domains.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/sea_esf_rad/aerosol.F90
aerosolrad_package.o: $(SRCROOT)atmos_param/sea_esf_rad/aerosolrad_package.F90 fms.o mpp_io.o time_manager.o diag_manager.o interpolator.o rad_utilities.o esfsw_parameters.o longwave_params.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/sea_esf_rad/aerosolrad_package.F90
age_of_air.o: $(SRCROOT)atmos_fv_dynamics/tools/age_of_air.F90
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_fv_dynamics/tools/age_of_air.F90
algebraiclength.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/algebraiclength.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/cppdefs.h                                                  \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/version.h turbulence.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/algebraiclength.F90
alpha_mnb.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/alpha_mnb.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/cppdefs.h                                                              \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/version.h turbulence.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/alpha_mnb.F90
amip_interp.o: $(SRCROOT)shared/amip_interp/amip_interp.F90 time_interp.o time_manager.o horiz_interp.o fms.o fms_io.o constants.o platform.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)shared/amip_interp/amip_interp.F90
array_lib.o: $(SRCROOT)atmos_param/cosp/quickbeam/array_lib.f90 mrgrnk.o
	$(FC) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/cosp/quickbeam/array_lib.f90
astronomy.o: $(SRCROOT)shared/astronomy/astronomy.F90 fms.o time_manager.o constants.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)shared/astronomy/astronomy.F90
atmos_age_tracer.o: $(SRCROOT)atmos_shared/tracer_driver/atmos_age_tracer.F90 fms.o time_manager.o diag_manager.o tracer_manager.o field_manager.o interpolator.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_shared/tracer_driver/atmos_age_tracer.F90
atmos_carbon_aerosol.o: $(SRCROOT)atmos_shared/tracer_driver/atmos_carbon_aerosol.F90 fms.o time_manager.o time_interp.o diag_manager.o tracer_manager.o field_manager.o atmos_tracer_utilities.o interpolator.o constants.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_shared/tracer_driver/atmos_carbon_aerosol.F90
atmos_ch3i.o: $(SRCROOT)atmos_shared/tracer_driver/atmos_ch3i.F90 fms.o field_manager.o tracer_manager.o time_manager.o diag_manager.o interpolator.o constants.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_shared/tracer_driver/atmos_ch3i.F90
atmos_co2.o: $(SRCROOT)atmos_shared/tracer_driver/atmos_co2.F90 fms.o tracer_manager.o field_manager.o diag_manager.o time_manager.o constants.o data_override.o mpp.o coupler_types.o atmos_ocean_fluxes.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_shared/tracer_driver/atmos_co2.F90
atmos_convection_tracer.o: $(SRCROOT)atmos_shared/tracer_driver/atmos_convection_tracer.F90 fms.o time_manager.o diag_manager.o tracer_manager.o field_manager.o atmos_tracer_utilities.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_shared/tracer_driver/atmos_convection_tracer.F90
atmos_dust.o: $(SRCROOT)atmos_shared/tracer_driver/atmos_dust.F90 fms.o time_manager.o diag_manager.o tracer_manager.o field_manager.o atmos_tracer_utilities.o interpolator.o constants.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_shared/tracer_driver/atmos_dust.F90
atmos_lib.o: $(SRCROOT)atmos_param/cosp/quickbeam/atmos_lib.f90
	$(FC) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/cosp/quickbeam/atmos_lib.f90
atmos_model.o: $(SRCROOT)atmos_coupled/atmos_model.F90 mpp.o mpp_domains.o fms.o fms_io.o time_manager.o field_manager.o tracer_manager.o diag_integral.o atmosphere.o xgrid.o coupler_types.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_coupled/atmos_model.F90
atmos_nudge.o: $(SRCROOT)atmos_shared/atmos_nudge/atmos_nudge.F90 fms.o time_manager.o data_override.o diag_manager.o mpp.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_shared/atmos_nudge/atmos_nudge.F90
atmos_ocean_fluxes.o: $(SRCROOT)shared/coupler/atmos_ocean_fluxes.F90 mpp.o coupler_types.o field_manager.o fm_util.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)shared/coupler/atmos_ocean_fluxes.F90
atmos_radon.o: $(SRCROOT)atmos_shared/tracer_driver/atmos_radon.F90 fms.o time_manager.o diag_manager.o tracer_manager.o field_manager.o atmos_tracer_utilities.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_shared/tracer_driver/atmos_radon.F90
atmos_sea_salt.o: $(SRCROOT)atmos_shared/tracer_driver/atmos_sea_salt.F90 fms.o time_manager.o diag_manager.o tracer_manager.o field_manager.o constants.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_shared/tracer_driver/atmos_sea_salt.F90
atmos_soa.o: $(SRCROOT)atmos_shared/tracer_driver/atmos_soa.F90 fms.o time_manager.o diag_manager.o tracer_manager.o field_manager.o constants.o interpolator.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_shared/tracer_driver/atmos_soa.F90
atmos_sulfate.o: $(SRCROOT)atmos_shared/tracer_driver/atmos_sulfate.F90 fms.o time_manager.o time_interp.o diag_manager.o tracer_manager.o field_manager.o interpolator.o constants.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_shared/tracer_driver/atmos_sulfate.F90
atmos_sulfur_hex.o: $(SRCROOT)atmos_shared/tracer_driver/atmos_sulfur_hex.F90 fms.o mpp.o time_manager.o diag_manager.o tracer_manager.o field_manager.o atmos_tracer_utilities.o constants.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_shared/tracer_driver/atmos_sulfur_hex.F90
atmos_tracer_driver.o: $(SRCROOT)atmos_shared/tracer_driver/atmos_tracer_driver.F90 fms.o time_manager.o diag_manager.o astronomy.o tracer_manager.o field_manager.o atmos_tracer_utilities.o constants.o atmos_radon.o atmos_carbon_aerosol.o                 \
atmos_convection_tracer.o atmos_sulfur_hex.o atmos_ch3i.o atmos_sea_salt.o atmos_dust.o atmos_sulfate.o atmos_soa.o tropchem_driver.o strat_chem_driver.o atmos_age_tracer.o atmos_co2.o interpolator.o coupler_types.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_shared/tracer_driver/atmos_tracer_driver.F90
atmos_tracer_utilities.o: $(SRCROOT)atmos_shared/tracer_driver/atmos_tracer_utilities.F90 fms.o time_manager.o diag_manager.o tracer_manager.o field_manager.o horiz_interp.o monin_obukhov.o constants.o interpolator.o astronomy.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_shared/tracer_driver/atmos_tracer_utilities.F90
atmosphere.o: $(SRCROOT)atmos_fv_dynamics/driver/coupled/atmosphere.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/atmos_fv_dynamics/model/fv_arrays.h /home/wenchang/scratch/tiger3/MOM4.1/src/atmos_fv_dynamics/model/fv_point.inc time_manager.o fms.o        \
fv_physics.o mpp_domains.o field_manager.o constants.o fv_pack.o fv_diagnostics.o timingModule.o fv_restart.o fv_dynamics.o fv_arrays.o mpp.o tracer_manager.o xgrid.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/atmos_fv_dynamics/model	$(SRCROOT)atmos_fv_dynamics/driver/coupled/atmosphere.F90
axis_utils.o: $(SRCROOT)shared/axis_utils/axis_utils.F90 mpp_io.o mpp.o fms.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)shared/axis_utils/axis_utils.F90
betaDistribution.o: $(SRCROOT)atmos_param/cloud_generator/betaDistribution.F90 fms.o mpp.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/cloud_generator/betaDistribution.F90
betts_miller.o: $(SRCROOT)atmos_param/betts_miller/betts_miller.F90 fms.o sat_vapor_pres.o constants.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/betts_miller/betts_miller.F90
bm_massflux.o: $(SRCROOT)atmos_param/betts_miller/bm_massflux.F90 fms.o sat_vapor_pres.o constants.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/betts_miller/bm_massflux.F90
bm_omp.o: $(SRCROOT)atmos_param/betts_miller/bm_omp.F90 fms.o sat_vapor_pres.o constants.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/betts_miller/bm_omp.F90
bulkphys_rad.o: $(SRCROOT)atmos_param/sea_esf_rad/bulkphys_rad.F90 fms.o rad_utilities.o rh_based_clouds.o diag_clouds_W.o strat_clouds_W.o standalone_clouds.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/sea_esf_rad/bulkphys_rad.F90
cg_drag.o: $(SRCROOT)atmos_param/cg_drag/cg_drag.F90 fms.o fms_io.o time_manager.o diag_manager.o constants.o column_diagnostics.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/cg_drag/cg_drag.F90
climap_albedo.o: $(SRCROOT)land_param/climap_albedo.F90 horiz_interp.o fms.o constants.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)land_param/climap_albedo.F90
cloud_generator.o: $(SRCROOT)atmos_param/cloud_generator/cloud_generator.F90 sat_vapor_pres.o constants.o fms.o random_numbers.o betaDistribution.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/cloud_generator/cloud_generator.F90
cloud_interpolator.o: $(SRCROOT)shared/drifters/cloud_interpolator.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/include/fms_platform.h
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/shared/include	$(SRCROOT)shared/drifters/cloud_interpolator.F90
cloud_obs.o: $(SRCROOT)atmos_param/cloud_obs/cloud_obs.F90 horiz_interp.o fms.o fms_io.o time_manager.o time_interp.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/cloud_obs/cloud_obs.F90
cloud_rad.o: $(SRCROOT)atmos_param/cloud_rad/cloud_rad.F90 fms.o constants.o diag_manager.o time_manager.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/cloud_rad/cloud_rad.F90
cloud_spec.o: $(SRCROOT)atmos_param/sea_esf_rad/cloud_spec.F90 time_manager.o fms.o tracer_manager.o field_manager.o data_override.o random_numbers.o cloud_generator.o constants.o rad_utilities.o esfsw_parameters.o strat_clouds_W.o diag_clouds_W.o        \
zetac_clouds_W.o specified_clouds_W.o rh_based_clouds.o donner_deep_clouds_W.o uw_clouds_W.o mgrp_prscr_clds.o standalone_clouds.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/sea_esf_rad/cloud_spec.F90
cloud_zonal.o: $(SRCROOT)atmos_param/cloud_zonal/cloud_zonal.F90 time_manager.o time_interp.o fms.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/cloud_zonal/cloud_zonal.F90
cloudrad_diagnostics.o: $(SRCROOT)atmos_param/sea_esf_rad/cloudrad_diagnostics.F90 fms.o time_manager.o diag_manager.o constants.o rad_utilities.o esfsw_parameters.o microphys_rad.o isccp_clouds.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/sea_esf_rad/cloudrad_diagnostics.F90
cloudrad_package.o: $(SRCROOT)atmos_param/sea_esf_rad/cloudrad_package.F90 fms.o time_manager.o rad_utilities.o esfsw_parameters.o cloudrad_diagnostics.o bulkphys_rad.o microphys_rad.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/sea_esf_rad/cloudrad_package.F90
clouds.o: $(SRCROOT)atmos_param/clouds/clouds.F90 cloud_rad.o cloud_zonal.o cloud_obs.o time_manager.o fms.o rh_clouds.o strat_cloud.o diag_cloud.o diag_manager.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/clouds/clouds.F90
cmue_a.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/cmue_a.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/cppdefs.h                                                                    \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/version.h turbulence.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/cmue_a.F90
cmue_b.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/cmue_b.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/cppdefs.h                                                                    \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/version.h turbulence.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/cmue_b.F90
cmue_c.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/cmue_c.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/cppdefs.h                                                                    \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/version.h turbulence.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/cmue_c.F90
cmue_d.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/cmue_d.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/cppdefs.h                                                                    \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/version.h turbulence.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/cmue_d.F90
cmue_ma.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/cmue_ma.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/cppdefs.h                                                                  \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/version.h turbulence.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/cmue_ma.F90
cmue_rf.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/cmue_rf.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/cppdefs.h                                                                  \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/version.h turbulence.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/cmue_rf.F90
cmue_sg.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/cmue_sg.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/cppdefs.h                                                                  \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/version.h turbulence.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/cmue_sg.F90
co2_data.o: $(SRCROOT)atmos_param/fsrad/co2_data.F90 fs_profile.o co2int.o fms.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/fsrad/co2_data.F90
co2int.o: $(SRCROOT)atmos_param/fsrad/co2int.F90 fs_profile.o fms.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/fsrad/co2int.F90
column_diagnostics.o: $(SRCROOT)shared/column_diagnostics/column_diagnostics.F90 mpp_io.o fms.o time_manager.o constants.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)shared/column_diagnostics/column_diagnostics.F90
compute_cpsi3.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/compute_cpsi3.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/cppdefs.h                                                      \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/version.h turbulence.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/compute_cpsi3.F90
compute_rist.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/compute_rist.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/cppdefs.h                                                        \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/version.h turbulence.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/compute_rist.F90
constants.o: $(SRCROOT)shared/constants/constants.F90
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)shared/constants/constants.F90
conv_closures.o: $(SRCROOT)atmos_param/shallow_cu/conv_closures.F90 fms.o conv_utilities_k.o conv_plumes_k.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/shallow_cu/conv_closures.F90
conv_plumes.o: $(SRCROOT)atmos_param/shallow_cu/conv_plumes.F90
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/shallow_cu/conv_plumes.F90
conv_plumes_k.o: $(SRCROOT)atmos_param/shallow_cu/conv_plumes_k.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/include/fms_platform.h aer_ccn_act_k.o conv_utilities_k.o sat_vapor_pres_k.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/shared/include	$(SRCROOT)atmos_param/shallow_cu/conv_plumes_k.F90
conv_utilities.o: $(SRCROOT)atmos_param/shallow_cu/conv_utilities.F90 constants.o fms.o conv_utilities_k.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/shallow_cu/conv_utilities.F90
conv_utilities_k.o: $(SRCROOT)atmos_param/shallow_cu/conv_utilities_k.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/include/fms_platform.h sat_vapor_pres_k.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/shared/include	$(SRCROOT)atmos_param/shallow_cu/conv_utilities_k.F90
convert_fluxes.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/convert_fluxes.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/cppdefs.h                                                          \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/version.h eqstate.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/convert_fluxes.F90
cosp.o: $(SRCROOT)atmos_param/cosp/cosp.f90 cosp_types.o cosp_simulator.o
	$(FC) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/cosp/cosp.f90
cosp_constants.o: $(SRCROOT)atmos_param/cosp/cosp_constants.f90
	$(FC) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/cosp/cosp_constants.f90
cosp_driver.o: $(SRCROOT)atmos_param/cosp/cosp_driver.F90 fms.o sat_vapor_pres.o time_manager.o diag_manager.o cosp_types.o cosp.o cosp_io.o cosp_constants.o lmd_ipsl_stats.o radar_simulator_types.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/cosp/cosp_driver.F90
cosp_io.o: $(SRCROOT)atmos_param/cosp/cosp_io.f90 cosp_constants.o cosp_types.o fms.o
	$(FC) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/cosp/cosp_io.f90
cosp_isccp_simulator.o: $(SRCROOT)atmos_param/cosp/cosp_isccp_simulator.f90 cosp_constants.o cosp_types.o
	$(FC) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/cosp/cosp_isccp_simulator.f90
cosp_lidar.o: $(SRCROOT)atmos_param/cosp/cosp_lidar.f90 cosp_constants.o cosp_types.o
	$(FC) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/cosp/cosp_lidar.f90
cosp_misr_simulator.o: $(SRCROOT)atmos_param/cosp/cosp_misr_simulator.f90 cosp_constants.o cosp_types.o
	$(FC) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/cosp/cosp_misr_simulator.f90
cosp_radar.o: $(SRCROOT)atmos_param/cosp/llnl/cosp_radar.f90 cosp_constants.o cosp_types.o radar_simulator_types.o array_lib.o atmos_lib.o format_input.o mrgrnk.o math_lib.o optics_lib.o
	$(FC) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/cosp/llnl/cosp_radar.f90
cosp_simulator.o: $(SRCROOT)atmos_param/cosp/cosp_simulator.f90 cosp_types.o cosp_radar.o cosp_lidar.o cosp_isccp_simulator.o cosp_misr_simulator.o cosp_stats.o
	$(FC) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/cosp/cosp_simulator.f90
cosp_stats.o: $(SRCROOT)atmos_param/cosp/cosp_stats.f90 cosp_constants.o cosp_types.o llnl_stats.o lmd_ipsl_stats.o
	$(FC) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/cosp/cosp_stats.f90
cosp_types.o: $(SRCROOT)atmos_param/cosp/cosp_types.f90 cosp_constants.o cosp_utils.o radar_simulator_types.o
	$(FC) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/cosp/cosp_types.f90
cosp_utils.o: $(SRCROOT)atmos_param/cosp/cosp_utils.f90 cosp_constants.o
	$(FC) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/cosp/cosp_utils.f90
coupler_main.o: /home/wenchang/scratch/tiger3/MOM4.1/src/coupler/coupler_main.F90 constants.o time_manager.o fms.o fms_io.o diag_manager.o field_manager.o tracer_manager.o coupler_types.o data_override.o atmos_model.o land_model.o ice_model.o             \
ocean_model.o flux_exchange.o atmos_tracer_driver.o mpp.o mpp_io.o mpp_domains.o memutils.o ensemble_manager.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	/home/wenchang/scratch/tiger3/MOM4.1/src/coupler/coupler_main.F90
coupler_types.o: $(SRCROOT)shared/coupler/coupler_types.F90 field_manager.o mpp.o fm_util.o time_manager.o diag_manager.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)shared/coupler/coupler_types.F90
create_xgrid.o: $(SRCROOT)shared/mosaic/create_xgrid.c /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mosaic/mosaic_util.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mosaic/create_xgrid.h                                                              \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mosaic/constant.h
	$(CC) $(CPPDEFS) $(CPPFLAGS) $(CFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mosaic	$(SRCROOT)shared/mosaic/create_xgrid.c
cu_mo_trans.o: $(SRCROOT)atmos_param/cu_mo_trans/cu_mo_trans.F90 constants.o fms.o diag_manager.o time_manager.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/cu_mo_trans/cu_mo_trans.F90
cumulus_closure_k.o: $(SRCROOT)atmos_param/donner_deep/cumulus_closure_k.F90 donner_types.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/donner_deep/cumulus_closure_k.F90
damping_driver.o: $(SRCROOT)atmos_param/damping_driver/damping_driver.F90 mg_drag.o cg_drag.o topo_drag.o fms.o diag_manager.o time_manager.o constants.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/damping_driver/damping_driver.F90
data_override.o: $(SRCROOT)shared/data_override/data_override.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/include/fms_platform.h platform.o constants.o mpp_io.o mpp.o horiz_interp.o time_interp_external.o fms_io.o fms.o axis_utils.o mpp_domains.o \
time_manager.o diag_manager.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/shared/include	$(SRCROOT)shared/data_override/data_override.F90
deep_conv.o: $(SRCROOT)atmos_param/shallow_cu/deep_conv.F90 fms.o constants.o conv_utilities.o conv_utilities_k.o conv_plumes_k.o conv_closures.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/shallow_cu/deep_conv.F90
diag_axis.o: $(SRCROOT)shared/diag_manager/diag_axis.F90 mpp_domains.o fms.o diag_data.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)shared/diag_manager/diag_axis.F90
diag_cloud.o: $(SRCROOT)atmos_param/diag_cloud/diag_cloud.F90 fms.o fms_io.o constants.o time_manager.o cloud_zonal.o diag_cloud_rad.o sat_vapor_pres.o shallow_conv.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/diag_cloud/diag_cloud.F90
diag_cloud_rad.o: $(SRCROOT)atmos_param/diag_cloud_rad/diag_cloud_rad.F90 fms.o cloud_rad.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/diag_cloud_rad/diag_cloud_rad.F90
diag_clouds_W.o: $(SRCROOT)atmos_param/sea_esf_rad/diag_clouds_W.F90 time_manager.o diag_cloud.o diag_cloud_rad.o fms.o rad_utilities.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/sea_esf_rad/diag_clouds_W.F90
diag_data.o: $(SRCROOT)shared/diag_manager/diag_data.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/include/fms_platform.h time_manager.o mpp_domains.o mpp_io.o fms.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/shared/include	$(SRCROOT)shared/diag_manager/diag_data.F90
diag_grid.o: $(SRCROOT)shared/diag_manager/diag_grid.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/include/fms_platform.h constants.o fms.o mpp.o mpp_domains.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/shared/include	$(SRCROOT)shared/diag_manager/diag_grid.F90
diag_integral.o: $(SRCROOT)atmos_param/diag_integral/diag_integral.F90 time_manager.o fms.o constants.o mpp.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/diag_integral/diag_integral.F90
diag_manager.o: $(SRCROOT)shared/diag_manager/diag_manager.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/include/fms_platform.h time_manager.o mpp_io.o fms.o mpp.o diag_axis.o diag_util.o diag_data.o diag_output.o diag_grid.o constants.o            \
mpp_domains.o fms_io.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/shared/include	$(SRCROOT)shared/diag_manager/diag_manager.F90
diag_output.o: $(SRCROOT)shared/diag_manager/diag_output.F90 mpp_io.o mpp_domains.o mpp.o diag_axis.o diag_data.o time_manager.o fms.o platform.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)shared/diag_manager/diag_output.F90
diag_util.o: $(SRCROOT)shared/diag_manager/diag_util.F90 diag_data.o diag_axis.o diag_output.o diag_grid.o fms.o fms_io.o mpp_domains.o time_manager.o mpp_io.o mpp.o constants.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)shared/diag_manager/diag_util.F90
diff_center.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/diff_center.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/cppdefs.h                                                                \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/version.h util.o tridiagonal_gotm.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/diff_center.F90
diff_face.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/diff_face.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/cppdefs.h                                                                    \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/version.h util.o tridiagonal_gotm.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/diff_face.F90
diffusivity.o: $(SRCROOT)atmos_param/diffusivity/diffusivity.F90 constants.o fms.o monin_obukhov.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/diffusivity/diffusivity.F90
dissipationeq.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/dissipationeq.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/cppdefs.h                                                      \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/version.h turbulence.o util.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/dissipationeq.F90
donner_cape_k.o: $(SRCROOT)atmos_param/donner_deep/donner_cape_k.F90 donner_types.o sat_vapor_pres_k.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/donner_deep/donner_cape_k.F90
donner_cloud_model_k.o: $(SRCROOT)atmos_param/donner_deep/donner_cloud_model_k.F90 donner_types.o sat_vapor_pres_k.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/donner_deep/donner_cloud_model_k.F90
donner_deep.o: $(SRCROOT)atmos_param/donner_deep/donner_deep.F90 donner_types.o conv_utilities_k.o conv_plumes_k.o fms_donner.o nonfms_donner.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/donner_deep/donner_deep.F90
donner_deep_clouds_W.o: $(SRCROOT)atmos_param/sea_esf_rad/donner_deep_clouds_W.F90 time_manager.o fms.o rad_utilities.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/sea_esf_rad/donner_deep_clouds_W.F90
donner_deep_k.o: $(SRCROOT)atmos_param/donner_deep/donner_deep_k.F90 donner_types.o conv_utilities_k.o conv_plumes_k.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/donner_deep/donner_deep_k.F90
donner_deep_miz.o: $(SRCROOT)atmos_param/donner_deep/donner_deep_miz.F90
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/donner_deep/donner_deep_miz.F90
donner_lite_k.o: $(SRCROOT)atmos_param/donner_deep/donner_lite_k.F90 donner_types.o conv_utilities_k.o conv_plumes_k.o sat_vapor_pres_k.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/donner_deep/donner_lite_k.F90
donner_lscloud_k.o: $(SRCROOT)atmos_param/donner_deep/donner_lscloud_k.F90 donner_types.o sat_vapor_pres_k.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/donner_deep/donner_lscloud_k.F90
donner_meso_k.o: $(SRCROOT)atmos_param/donner_deep/donner_meso_k.F90 donner_types.o sat_vapor_pres_k.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/donner_deep/donner_meso_k.F90
donner_rad_k.o: $(SRCROOT)atmos_param/donner_deep/donner_rad_k.F90 donner_types.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/donner_deep/donner_rad_k.F90
donner_types.o: $(SRCROOT)atmos_param/donner_deep/donner_types.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/atmos_param/donner_deep/donner_types.h
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/atmos_param/donner_deep	$(SRCROOT)atmos_param/donner_deep/donner_types.F90
donner_utilities_k.o: $(SRCROOT)atmos_param/donner_deep/donner_utilities_k.F90 donner_types.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/donner_deep/donner_utilities_k.F90
drifters.o: $(SRCROOT)shared/drifters/drifters.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/include/fms_platform.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/drifters/fms_switches.h                                                              \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/drifters/drifters_push.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/drifters/drifters_set_field.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/drifters/drifters_compute_k.h mpp.o mpp_domains.o       \
drifters_core.o drifters_input.o drifters_io.o drifters_comm.o cloud_interpolator.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/shared/include -I/home/wenchang/scratch/tiger3/MOM4.1/src/shared/drifters	$(SRCROOT)shared/drifters/drifters.F90
drifters_comm.o: $(SRCROOT)shared/drifters/drifters_comm.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/include/fms_platform.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/drifters/fms_switches.h mpp.o mpp_domains.o drifters_core.o                \
drifters_input.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/shared/include -I/home/wenchang/scratch/tiger3/MOM4.1/src/shared/drifters	$(SRCROOT)shared/drifters/drifters_comm.F90
drifters_core.o: $(SRCROOT)shared/drifters/drifters_core.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/include/fms_platform.h
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/shared/include	$(SRCROOT)shared/drifters/drifters_core.F90
drifters_input.o: $(SRCROOT)shared/drifters/drifters_input.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/include/fms_platform.h
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/shared/include	$(SRCROOT)shared/drifters/drifters_input.F90
drifters_io.o: $(SRCROOT)shared/drifters/drifters_io.F90
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)shared/drifters/drifters_io.F90
dry_adj.o: $(SRCROOT)atmos_param/dry_adj/dry_adj.F90 fms.o constants.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/dry_adj/dry_adj.F90
dsd.o: $(SRCROOT)atmos_param/cosp/quickbeam/dsd.f90 array_lib.o math_lib.o
	$(FC) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/cosp/quickbeam/dsd.f90
dyn_core.o: $(SRCROOT)atmos_fv_dynamics/model/dyn_core.F90 fv_pack.o shr_kind_mod.o pft_module.o sw_core.o timingModule.o mod_comm.o fv_arrays.o pmaxmin.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_fv_dynamics/model/dyn_core.F90
ecmfft.o: $(SRCROOT)atmos_fv_dynamics/model/ecmfft.F90
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_fv_dynamics/model/ecmfft.F90
edt.o: $(SRCROOT)atmos_param/edt/edt.F90 constants.o fms.o diag_manager.o time_manager.o monin_obukhov.o sat_vapor_pres.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/edt/edt.F90
ensemble_manager.o: $(SRCROOT)shared/coupler/ensemble_manager.F90 fms.o mpp.o fms_io.o diag_manager.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)shared/coupler/ensemble_manager.F90
entrain.o: $(SRCROOT)atmos_param/entrain/entrain.F90 constants.o fms.o diag_manager.o time_manager.o sat_vapor_pres.o monin_obukhov.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/entrain/entrain.F90
epsbalgebraic.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/epsbalgebraic.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/cppdefs.h                                                      \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/version.h turbulence.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/epsbalgebraic.F90
eqstate.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/eqstate.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/cppdefs.h                                                                        \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/version.h
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/eqstate.F90
esfsw_driver.o: $(SRCROOT)atmos_param/sea_esf_rad/esfsw_driver.F90 fms.o constants.o esfsw_parameters.o rad_utilities.o tracer_manager.o field_manager.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/sea_esf_rad/esfsw_driver.F90
esfsw_parameters.o: $(SRCROOT)atmos_param/sea_esf_rad/esfsw_parameters.F90 fms.o rad_utilities.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/sea_esf_rad/esfsw_parameters.F90
fft.o: $(SRCROOT)shared/fft/fft.F90 platform.o fms.o fft99.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)shared/fft/fft.F90
fft99.o: $(SRCROOT)shared/fft/fft99.F90 constants.o mpp.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)shared/fft/fft99.F90
field_manager.o: $(SRCROOT)shared/field_manager/field_manager.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/field_manager/parse.inc mpp.o mpp_io.o fms.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/shared/field_manager	$(SRCROOT)shared/field_manager/field_manager.F90
fill_module.o: $(SRCROOT)atmos_fv_dynamics/model/fill_module.F90
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_fv_dynamics/model/fill_module.F90
fk_craig.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/fk_craig.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/cppdefs.h                                                                \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/version.h
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/fk_craig.F90
flux_exchange.o: /home/wenchang/scratch/tiger3/MOM4.1/src/coupler/flux_exchange.F90 mpp.o mpp_domains.o mpp_io.o atmos_model.o ocean_model.o ice_model.o land_model.o surface_flux.o monin_obukhov.o xgrid.o diag_integral.o diag_manager.o time_manager.o     \
sat_vapor_pres.o constants.o fms.o data_override.o coupler_types.o atmos_ocean_fluxes.o atmos_tracer_driver.o field_manager.o tracer_manager.o stock_constants.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	/home/wenchang/scratch/tiger3/MOM4.1/src/coupler/flux_exchange.F90
fm_util.o: $(SRCROOT)shared/field_manager/fm_util.F90 field_manager.o fms.o mpp.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)shared/field_manager/fm_util.F90
fms.o: $(SRCROOT)shared/fms/fms.F90 mpp.o mpp_domains.o mpp_io.o fms_io.o memutils.o constants.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)shared/fms/fms.F90
fms_donner.o: $(SRCROOT)atmos_param/donner_deep/fms_donner.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/atmos_param/donner_deep/donner_nml.h time_manager.o diag_manager.o field_manager.o tracer_manager.o atmos_tracer_utilities.o sat_vapor_pres.o fms.o    \
fms_io.o mpp_io.o constants.o column_diagnostics.o donner_types.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/atmos_param/donner_deep	$(SRCROOT)atmos_param/donner_deep/fms_donner.F90
fms_io.o: $(SRCROOT)shared/fms/fms_io.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/include/fms_platform.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/fms/read_data_2d.inc /home/wenchang/scratch/tiger3/MOM4.1/src/shared/fms/read_data_3d.inc     \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/fms/read_data_4d.inc /home/wenchang/scratch/tiger3/MOM4.1/src/shared/fms/write_data.inc mpp_io.o mpp_domains.o mpp.o platform.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/shared/include -I/home/wenchang/scratch/tiger3/MOM4.1/src/shared/fms	$(SRCROOT)shared/fms/fms_io.F90
format_input.o: $(SRCROOT)atmos_param/cosp/quickbeam/format_input.f90 array_lib.o
	$(FC) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/cosp/quickbeam/format_input.f90
fs_profile.o: $(SRCROOT)atmos_param/fsrad/fs_profile.F90 fms.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/fsrad/fs_profile.F90
fsrad.o: $(SRCROOT)atmos_param/fsrad/fsrad.F90 mcm_lw.o mcm_sw_driver.o shortwave.o longwave.o rdparm.o rad_diag.o co2_data.o fms.o constants.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/fsrad/fsrad.F90
fv_arrays.o: $(SRCROOT)atmos_fv_dynamics/model/fv_arrays.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/include/fms_platform.h /home/wenchang/scratch/tiger3/MOM4.1/src/atmos_fv_dynamics/model/fv_point.inc mpp.o mpp_domains.o mpp_pset.o mod_comm.o    \
ensemble_manager.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/shared/include -I/home/wenchang/scratch/tiger3/MOM4.1/src/atmos_fv_dynamics/model	$(SRCROOT)atmos_fv_dynamics/model/fv_arrays.F90
fv_diagnostics.o: $(SRCROOT)atmos_fv_dynamics/tools/fv_diagnostics.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/atmos_fv_dynamics/model/fv_arrays.h /home/wenchang/scratch/tiger3/MOM4.1/src/atmos_fv_dynamics/model/fv_point.inc diag_manager.o constants.o   \
time_manager.o fms.o mpp_domains.o fv_pack.o tracer_manager.o field_manager.o mpp.o fv_arrays.o pmaxmin.o pv_module.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/atmos_fv_dynamics/model	$(SRCROOT)atmos_fv_dynamics/tools/fv_diagnostics.F90
fv_dynamics.o: $(SRCROOT)atmos_fv_dynamics/model/fv_dynamics.F90 fv_pack.o mapz_module.o dyn_core.o pft_module.o timingModule.o mod_comm.o time_manager.o fv_arrays.o shr_kind_mod.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_fv_dynamics/model/fv_dynamics.F90
fv_pack.o: $(SRCROOT)atmos_fv_dynamics/model/fv_pack.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/atmos_fv_dynamics/model/fv_arrays.h /home/wenchang/scratch/tiger3/MOM4.1/src/atmos_fv_dynamics/model/fv_point.inc timingModule.o shr_kind_mod.o mod_comm.o   \
fms.o mpp.o mpp_domains.o constants.o tracer_manager.o field_manager.o fv_arrays.o pft_module.o fms_io.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/atmos_fv_dynamics/model	$(SRCROOT)atmos_fv_dynamics/model/fv_pack.F90
fv_physics.o: $(SRCROOT)atmos_fv_dynamics/driver/coupled/fv_physics.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/atmos_fv_dynamics/model/fv_arrays.h /home/wenchang/scratch/tiger3/MOM4.1/src/atmos_fv_dynamics/model/fv_point.inc time_manager.o fms.o        \
physics_driver.o field_manager.o tracer_manager.o fv_pack.o timingModule.o atmos_co2.o atmos_nudge.o constants.o mpp.o update_fv_phys.o fv_arrays.o mpp_domains.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/atmos_fv_dynamics/model	$(SRCROOT)atmos_fv_dynamics/driver/coupled/fv_physics.F90
fv_restart.o: $(SRCROOT)atmos_fv_dynamics/tools/fv_restart.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/atmos_fv_dynamics/model/fv_arrays.h /home/wenchang/scratch/tiger3/MOM4.1/src/atmos_fv_dynamics/model/fv_point.inc fms.o fms_io.o mpp_io.o fv_pack.o    \
tracer_manager.o field_manager.o platform.o mod_comm.o fv_arrays.o mpp.o mpp_domains.o constants.o pmaxmin.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/atmos_fv_dynamics/model	$(SRCROOT)atmos_fv_dynamics/tools/fv_restart.F90
gas_tf.o: $(SRCROOT)atmos_param/sea_esf_rad/gas_tf.F90 fms.o constants.o rad_utilities.o longwave_params.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/sea_esf_rad/gas_tf.F90
gases.o: $(SRCROOT)atmos_param/cosp/quickbeam/gases.f90
	$(FC) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/cosp/quickbeam/gases.f90
gaussian_topog.o: $(SRCROOT)shared/topography/gaussian_topog.F90 fms.o constants.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)shared/topography/gaussian_topog.F90
generic_BLING.o: /home/wenchang/scratch/tiger3/MOM4.1/src/ocean_shared/generic_tracers/generic_BLING.F90 coupler_types.o field_manager.o mpp.o fms.o time_manager.o fm_util.o diag_manager.o constants.o generic_tracer_utils.o FMS_ocmip2_co2calc.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	/home/wenchang/scratch/tiger3/MOM4.1/src/ocean_shared/generic_tracers/generic_BLING.F90
generic_CFC.o: /home/wenchang/scratch/tiger3/MOM4.1/src/ocean_shared/generic_tracers/generic_CFC.F90 coupler_types.o field_manager.o mpp.o time_manager.o fm_util.o generic_tracer_utils.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	/home/wenchang/scratch/tiger3/MOM4.1/src/ocean_shared/generic_tracers/generic_CFC.F90
generic_TOPAZ.o: /home/wenchang/scratch/tiger3/MOM4.1/src/ocean_shared/generic_tracers/generic_TOPAZ.F90 coupler_types.o field_manager.o mpp.o time_manager.o fm_util.o diag_manager.o constants.o generic_tracer_utils.o FMS_ocmip2_co2calc.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	/home/wenchang/scratch/tiger3/MOM4.1/src/ocean_shared/generic_tracers/generic_TOPAZ.F90
generic_tracer.o: /home/wenchang/scratch/tiger3/MOM4.1/src/ocean_shared/generic_tracers/generic_tracer.F90 fms.o field_manager.o mpp.o time_manager.o coupler_types.o generic_tracer_utils.o generic_CFC.o generic_TOPAZ.o generic_BLING.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	/home/wenchang/scratch/tiger3/MOM4.1/src/ocean_shared/generic_tracers/generic_tracer.F90
generic_tracer_utils.o: /home/wenchang/scratch/tiger3/MOM4.1/src/ocean_shared/generic_tracers/generic_tracer_utils.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/include/fms_platform.h coupler_types.o FMS_coupler_util.o atmos_ocean_fluxes.o mpp.o    \
time_manager.o diag_manager.o field_manager.o fms.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/shared/include	/home/wenchang/scratch/tiger3/MOM4.1/src/ocean_shared/generic_tracers/generic_tracer_utils.F90
genericeq.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/genericeq.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/cppdefs.h                                                              \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/version.h turbulence.o util.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/genericeq.F90
get_cal_time.o: $(SRCROOT)shared/time_manager/get_cal_time.F90 fms.o time_manager.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)shared/time_manager/get_cal_time.F90
getmax.o: $(SRCROOT)atmos_fv_dynamics/tools/getmax.F90 mod_comm.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_fv_dynamics/tools/getmax.F90
gmean.o: $(SRCROOT)atmos_fv_dynamics/tools/gmean.F90 fv_pack.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_fv_dynamics/tools/gmean.F90
gotm_lib_version.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/gotm_lib_version.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/cppdefs.h                                                \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/version.h
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/gotm_lib_version.F90
gradient.o: $(SRCROOT)shared/mosaic/gradient.F90 mpp.o constants.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)shared/mosaic/gradient.F90
gradient_c2l.o: $(SRCROOT)shared/mosaic/gradient_c2l.c /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mosaic/constant.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mosaic/mosaic_util.h                                                                  \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mosaic/gradient_c2l.h
	$(CC) $(CPPDEFS) $(CPPFLAGS) $(CFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mosaic	$(SRCROOT)shared/mosaic/gradient_c2l.c
grey_radiation.o: $(SRCROOT)atmos_param/grey_radiation/grey_radiation.F90 fms.o constants.o astronomy.o diag_manager.o time_manager.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/grey_radiation/grey_radiation.F90
grid.o: $(SRCROOT)shared/mosaic/grid.F90 constants.o fms.o mosaic.o mpp_domains.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)shared/mosaic/grid.F90
gridinterpol.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/gridinterpol.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/cppdefs.h                                                              \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/version.h
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/gridinterpol.F90
hconst.o: $(SRCROOT)atmos_param/fsrad/hconst.F90
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/fsrad/hconst.F90
horiz_interp.o: $(SRCROOT)shared/horiz_interp/horiz_interp.F90 fms.o mpp.o constants.o horiz_interp_type.o horiz_interp_conserve.o horiz_interp_bilinear.o horiz_interp_bicubic.o horiz_interp_spherical.o mpp_io.o mpp_domains.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)shared/horiz_interp/horiz_interp.F90
horiz_interp_bicubic.o: $(SRCROOT)shared/horiz_interp/horiz_interp_bicubic.F90 mpp.o fms.o horiz_interp_type.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)shared/horiz_interp/horiz_interp_bicubic.F90
horiz_interp_bilinear.o: $(SRCROOT)shared/horiz_interp/horiz_interp_bilinear.F90 mpp.o fms.o constants.o horiz_interp_type.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)shared/horiz_interp/horiz_interp_bilinear.F90
horiz_interp_conserve.o: $(SRCROOT)shared/horiz_interp/horiz_interp_conserve.F90 mpp.o fms.o constants.o horiz_interp_type.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)shared/horiz_interp/horiz_interp_conserve.F90
horiz_interp_spherical.o: $(SRCROOT)shared/horiz_interp/horiz_interp_spherical.F90 mpp.o fms.o constants.o horiz_interp_type.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)shared/horiz_interp/horiz_interp_spherical.F90
horiz_interp_type.o: $(SRCROOT)shared/horiz_interp/horiz_interp_type.F90 mpp.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)shared/horiz_interp/horiz_interp_type.F90
hs_forcing.o: $(SRCROOT)atmos_param/hs_forcing/hs_forcing.F90 constants.o fms.o time_manager.o diag_manager.o field_manager.o tracer_manager.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/hs_forcing/hs_forcing.F90
icarus.o: $(SRCROOT)atmos_param/cosp/icarus-scops-3.7/icarus.f
	$(FC) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/cosp/icarus-scops-3.7/icarus.f
ice_albedo.o: /home/wenchang/scratch/tiger3/MOM4.1/src/ice_param/ice_albedo.F90 fms.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	/home/wenchang/scratch/tiger3/MOM4.1/src/ice_param/ice_albedo.F90
ice_bergs.o: /home/wenchang/scratch/tiger3/MOM4.1/src/ice_sis/ice_bergs.F90 constants.o fms.o mosaic.o mpp.o mpp_domains.o time_manager.o diag_manager.o random_numbers.o stock_constants.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	/home/wenchang/scratch/tiger3/MOM4.1/src/ice_sis/ice_bergs.F90
ice_dyn.o: /home/wenchang/scratch/tiger3/MOM4.1/src/ice_sis/ice_dyn.F90 mpp_domains.o constants.o ice_grid.o ice_thm.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	/home/wenchang/scratch/tiger3/MOM4.1/src/ice_sis/ice_dyn.F90
ice_grid.o: /home/wenchang/scratch/tiger3/MOM4.1/src/ice_sis/ice_grid.F90 constants.o mpp.o mpp_domains.o fms.o mosaic.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	/home/wenchang/scratch/tiger3/MOM4.1/src/ice_sis/ice_grid.F90
ice_model.o: /home/wenchang/scratch/tiger3/MOM4.1/src/ice_sis/ice_model.F90 mpp.o mpp_domains.o fms.o diag_manager.o time_manager.o astronomy.o coupler_types.o constants.o ocean_albedo.o ocean_rough.o ice_type.o ice_grid.o ice_spec.o ice_thm.o ice_dyn.o  \
ice_bergs.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	/home/wenchang/scratch/tiger3/MOM4.1/src/ice_sis/ice_model.F90
ice_spec.o: /home/wenchang/scratch/tiger3/MOM4.1/src/ice_sis/ice_spec.F90 fms.o time_manager.o data_override.o constants.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	/home/wenchang/scratch/tiger3/MOM4.1/src/ice_sis/ice_spec.F90
ice_thm.o: /home/wenchang/scratch/tiger3/MOM4.1/src/ice_sis/ice_thm.F90 constants.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	/home/wenchang/scratch/tiger3/MOM4.1/src/ice_sis/ice_thm.F90
ice_type.o: /home/wenchang/scratch/tiger3/MOM4.1/src/ice_sis/ice_type.F90 mpp.o mpp_domains.o fms.o fms_io.o diag_manager.o time_manager.o coupler_types.o constants.o ice_grid.o ice_thm.o ice_dyn.o ice_bergs.o astronomy.o stock_constants.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	/home/wenchang/scratch/tiger3/MOM4.1/src/ice_sis/ice_type.F90
init_dry_atm.o: $(SRCROOT)atmos_fv_dynamics/tools/init_dry_atm.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/atmos_fv_dynamics/model/fv_arrays.h /home/wenchang/scratch/tiger3/MOM4.1/src/atmos_fv_dynamics/model/fv_point.inc fv_pack.o fms.o mod_comm.o       \
mpp_io.o fv_arrays.o pmaxmin.o constants.o shr_kind_mod.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/atmos_fv_dynamics/model	$(SRCROOT)atmos_fv_dynamics/tools/init_dry_atm.F90
init_sw_ic.o: $(SRCROOT)atmos_fv_dynamics/tools/init_sw_ic.F90 fv_pack.o pv_module.o mod_comm.o shr_kind_mod.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_fv_dynamics/tools/init_sw_ic.F90
internal_wave.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/internal_wave.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/cppdefs.h                                                      \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/version.h turbulence.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/internal_wave.F90
interp.o: $(SRCROOT)shared/mosaic/interp.c /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mosaic/mosaic_util.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mosaic/interp.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mosaic/create_xgrid.h
	$(CC) $(CPPDEFS) $(CPPFLAGS) $(CFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mosaic	$(SRCROOT)shared/mosaic/interp.c
interpolator.o: $(SRCROOT)atmos_shared/interpolator/interpolator.F90 mpp.o mpp_io.o mpp_domains.o diag_manager.o fms.o horiz_interp.o time_manager.o time_interp.o constants.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_shared/interpolator/interpolator.F90
isccp_cloud_types.o: $(SRCROOT)atmos_param/cosp/icarus-scops-3.7/isccp_cloud_types.f
	$(FC) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/cosp/icarus-scops-3.7/isccp_cloud_types.f
isccp_clouds.o: $(SRCROOT)atmos_param/sea_esf_rad/isccp_clouds.F90 fms.o time_manager.o diag_manager.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/sea_esf_rad/isccp_clouds.F90
ispralength.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/ispralength.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/cppdefs.h                                                          \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/version.h turbulence.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/ispralength.F90
kbalgebraic.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/kbalgebraic.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/cppdefs.h                                                          \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/version.h turbulence.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/kbalgebraic.F90
kbeq.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/kbeq.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/cppdefs.h                                                                        \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/version.h turbulence.o util.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/kbeq.F90
kpp.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/kpp.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/cppdefs.h                                                                          \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/version.h turbulence.o eqstate.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/kpp.F90
lagrange.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/lagrange.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/cppdefs.h                                                                      \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/version.h
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/lagrange.F90
land_model.o: $(SRCROOT)land_lad/land_model.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/include/fms_platform.h time_manager.o mpp_domains.o fms.o vegetation.o soil.o land_types.o numerics.o constants.o diag_manager.o field_manager.o               \
tracer_manager.o mosaic.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/shared/include	$(SRCROOT)land_lad/land_model.F90
land_properties.o: $(SRCROOT)land_lad/soil/land_properties.F90 mpp_domains.o time_manager.o mpp_io.o fms.o constants.o horiz_interp.o numerics.o climap_albedo.o diag_manager.o topography.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)land_lad/soil/land_properties.F90
land_types.o: $(SRCROOT)land_lad/land_types.F90 mpp_domains.o fms.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)land_lad/land_types.F90
lengthscaleeq.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/lengthscaleeq.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/cppdefs.h                                                      \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/version.h turbulence.o util.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/lengthscaleeq.F90
lhsw_driver.o: $(SRCROOT)atmos_param/sea_esf_rad/lhsw_driver.F90 rad_utilities.o constants.o fms.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/sea_esf_rad/lhsw_driver.F90
lidar_simulator.o: $(SRCROOT)atmos_param/cosp/actsim/lidar_simulator.f90
	$(FC) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/cosp/actsim/lidar_simulator.f90
lin_cloud_microphys.o: $(SRCROOT)atmos_param/lin_cloud_microphys/lin_cloud_microphys.F90 mpp.o diag_manager.o time_manager.o constants.o fms.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/lin_cloud_microphys/lin_cloud_microphys.F90
llnl_stats.o: $(SRCROOT)atmos_param/cosp/llnl/llnl_stats.f90
	$(FC) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/cosp/llnl/llnl_stats.f90
lmd_ipsl_stats.o: $(SRCROOT)atmos_param/cosp/actsim/lmd_ipsl_stats.f90 llnl_stats.o cosp_constants.o
	$(FC) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/cosp/actsim/lmd_ipsl_stats.f90
load_hydrometeor_classes.o: $(SRCROOT)atmos_param/cosp/quickbeam/load_hydrometeor_classes.f90 radar_simulator_types.o
	$(FC) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/cosp/quickbeam/load_hydrometeor_classes.f90
load_mie_table.o: $(SRCROOT)atmos_param/cosp/quickbeam/load_mie_table.f90 radar_simulator_types.o
	$(FC) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/cosp/quickbeam/load_mie_table.f90
longwave.o: $(SRCROOT)atmos_param/fsrad/longwave.F90 rdparm.o hconst.o fms.o co2_data.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/fsrad/longwave.F90
longwave_clouds.o: $(SRCROOT)atmos_param/sea_esf_rad/longwave_clouds.F90 fms.o constants.o rad_utilities.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/sea_esf_rad/longwave_clouds.F90
longwave_driver.o: $(SRCROOT)atmos_param/sea_esf_rad/longwave_driver.F90 fms.o time_manager.o rad_utilities.o sealw99.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/sea_esf_rad/longwave_driver.F90
longwave_fluxes.o: $(SRCROOT)atmos_param/sea_esf_rad/longwave_fluxes.F90 fms.o rad_utilities.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/sea_esf_rad/longwave_fluxes.F90
longwave_params.o: $(SRCROOT)atmos_param/sea_esf_rad/longwave_params.F90 fms.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/sea_esf_rad/longwave_params.F90
longwave_tables.o: $(SRCROOT)atmos_param/sea_esf_rad/longwave_tables.F90 fms.o rad_utilities.o longwave_params.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/sea_esf_rad/longwave_tables.F90
lscale_cond.o: $(SRCROOT)atmos_param/lscale_cond/lscale_cond.F90 fms.o sat_vapor_pres.o constants.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/lscale_cond/lscale_cond.F90
lw_gases_stdtf.o: $(SRCROOT)atmos_param/sea_esf_rad/lw_gases_stdtf.F90 fms.o fms_io.o rad_utilities.o gas_tf.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/sea_esf_rad/lw_gases_stdtf.F90
m_tracname.o: $(SRCROOT)atmos_shared/tracer_driver/tropchem/m_tracname.F90 moz.mods.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_shared/tracer_driver/tropchem/m_tracname.F90
mapz_module.o: $(SRCROOT)atmos_fv_dynamics/model/mapz_module.F90 fv_pack.o fill_module.o fv_diagnostics.o diag_manager.o mod_comm.o time_manager.o fv_arrays.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_fv_dynamics/model/mapz_module.F90
mask.o: /home/wenchang/scratch/tiger3/MOM4.1/src/ice_sis/mask.F90 rot.o fms.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	/home/wenchang/scratch/tiger3/MOM4.1/src/ice_sis/mask.F90
math_lib.o: $(SRCROOT)atmos_param/cosp/quickbeam/math_lib.f90 mrgrnk.o array_lib.o
	$(FC) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/cosp/quickbeam/math_lib.f90
mcm_lw.o: $(SRCROOT)atmos_param/fsrad/mcm_lw.F90 constants.o fms.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/fsrad/mcm_lw.F90
mcm_sw_driver.o: $(SRCROOT)atmos_param/fsrad/mcm_sw_driver.F90 fms.o mcm_swnew.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/fsrad/mcm_sw_driver.F90
mcm_swnew.o: $(SRCROOT)atmos_param/fsrad/mcm_swnew.F90 mcm_swtbls.o fms.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/fsrad/mcm_swnew.F90
mcm_swtbls.o: $(SRCROOT)atmos_param/fsrad/mcm_swtbls.F90
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/fsrad/mcm_swtbls.F90
memuse.o: $(SRCROOT)shared/memutils/memuse.c
	$(CC) $(CPPDEFS) $(CPPFLAGS) $(CFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)shared/memutils/memuse.c
memutils.o: $(SRCROOT)shared/memutils/memutils.F90 mpp.o mpp_io.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)shared/memutils/memutils.F90
mg_drag.o: $(SRCROOT)atmos_param/mg_drag/mg_drag.F90 topography.o fms.o fms_io.o constants.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/mg_drag/mg_drag.F90
mgrp_prscr_clds.o: $(SRCROOT)atmos_param/sea_esf_rad/mgrp_prscr_clds.F90 fms.o constants.o rad_utilities.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/sea_esf_rad/mgrp_prscr_clds.F90
microphys_cloud.o: $(SRCROOT)atmos_param/sea_esf_rad/microphys_cloud.F90 fms.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/sea_esf_rad/microphys_cloud.F90
microphys_rad.o: $(SRCROOT)atmos_param/sea_esf_rad/microphys_rad.F90 fms.o constants.o time_manager.o diag_manager.o random_numbers.o cloud_generator.o rad_utilities.o longwave_params.o esfsw_parameters.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/sea_esf_rad/microphys_rad.F90
mo_chem_utls.o: $(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_chem_utls.F90 moz.mods.o m_tracname.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_chem_utls.F90
mo_chemdr.o: $(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_chemdr.F90 moz.mods.o mo_photo.o mo_exp_slv.o mo_imp_slv.o mo_rodas_slv.o mo_usrrxt.o mo_setinv.o moz.subs.o mo_setsox.o mo_chem_utls.o time_manager.o strat_chem_utilities.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_chemdr.F90
mo_chemini.o: $(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_chemini.F90 mo_photo.o mo_chem_utls.o mo_usrrxt.o moz.mods.o mo_exp_slv.o mo_imp_slv.o mo_rodas_slv.o mo_read_sim_chm.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_chemini.F90
mo_exp_slv.o: $(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_exp_slv.F90 moz.mods.o mo_chem_utls.o moz.mat.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_exp_slv.F90
mo_hook.o: $(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_hook.F90 diag_manager.o time_manager.o constants.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_hook.F90
mo_imp_slv.o: $(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_imp_slv.F90 moz.mods.o constants.o mo_chem_utls.o m_tracname.o moz.mat.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_imp_slv.F90
mo_jpl.o: $(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_jpl.F90
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_jpl.F90
mo_photo.o: $(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_photo.F90 mpp.o mpp_io.o time_manager.o constants.o mo_chem_utls.o moz.mods.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_photo.F90
mo_read_sim_chm.o: $(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_read_sim_chm.F90 mpp.o mpp_io.o moz.mods.o m_tracname.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_read_sim_chm.F90
mo_rodas_slv.o: $(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_rodas_slv.F90 moz.mods.o mo_chem_utls.o moz.mat.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_rodas_slv.F90
mo_setinv.o: $(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_setinv.F90
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_setinv.F90
mo_setsox.o: $(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_setsox.F90 mo_chem_utls.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_setsox.F90
mo_usrrxt.o: $(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_usrrxt.F90 sat_vapor_pres.o constants.o strat_chem_utilities.o mo_chem_utls.o moz.mods.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_usrrxt.F90
mod_comm.o: $(SRCROOT)atmos_fv_dynamics/tools/mod_comm.F90 timingModule.o shr_kind_mod.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_fv_dynamics/tools/mod_comm.F90
moist_conv.o: $(SRCROOT)atmos_param/moist_conv/moist_conv.F90 mpp.o time_manager.o diag_manager.o sat_vapor_pres.o fms.o constants.o field_manager.o tracer_manager.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/moist_conv/moist_conv.F90
moist_processes.o: $(SRCROOT)atmos_param/moist_processes/moist_processes.F90 sat_vapor_pres.o time_manager.o diag_manager.o fms.o field_manager.o tracer_manager.o constants.o betts_miller.o bm_massflux.o bm_omp.o donner_deep.o moist_conv.o lscale_cond.o  \
uw_conv.o lin_cloud_microphys.o ras.o dry_adj.o strat_cloud.o rh_clouds.o diag_cloud.o diag_integral.o cu_mo_trans.o mo_hook.o rad_utilities.o moist_processes_utils.o moistproc_kernels.o atmos_tracer_utilities.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/moist_processes/moist_processes.F90
moist_processes_utils.o: $(SRCROOT)atmos_param/moist_processes/moist_processes_utils.F90 sat_vapor_pres.o time_manager.o diag_manager.o constants.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/moist_processes/moist_processes_utils.F90
moistproc_kernels.o: $(SRCROOT)atmos_param/moist_processes/moistproc_kernels.F90 sat_vapor_pres.o time_manager.o diag_manager.o constants.o field_manager.o tracer_manager.o betts_miller.o bm_massflux.o bm_omp.o diag_cloud.o donner_deep.o moist_conv.o     \
lscale_cond.o uw_conv.o lin_cloud_microphys.o ras.o strat_cloud.o rh_clouds.o cu_mo_trans.o atmos_tracer_utilities.o mo_hook.o rad_utilities.o moist_processes_utils.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/moist_processes/moistproc_kernels.F90
monin_obukhov.o: $(SRCROOT)atmos_param/monin_obukhov/monin_obukhov.F90 constants.o fms.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/monin_obukhov/monin_obukhov.F90
monin_obukhov_kernel.o: $(SRCROOT)atmos_param/monin_obukhov/monin_obukhov_kernel.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/include/fms_platform.h /home/wenchang/scratch/tiger3/MOM4.1/src/atmos_param/monin_obukhov/monin_obukhov_interfaces.h
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/shared/include -I/home/wenchang/scratch/tiger3/MOM4.1/src/atmos_param/monin_obukhov	$(SRCROOT)atmos_param/monin_obukhov/monin_obukhov_kernel.F90
mosaic.o: $(SRCROOT)shared/mosaic/mosaic.F90 mpp.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)shared/mosaic/mosaic.F90
mosaic_util.o: $(SRCROOT)shared/mosaic/mosaic_util.c /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mosaic/mosaic_util.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mosaic/constant.h
	$(CC) $(CPPDEFS) $(CPPFLAGS) $(CFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mosaic	$(SRCROOT)shared/mosaic/mosaic_util.c
moz.mat.o: $(SRCROOT)atmos_shared/tracer_driver/tropchem/moz.mat.F90 moz.mods.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_shared/tracer_driver/tropchem/moz.mat.F90
moz.mods.o: $(SRCROOT)atmos_shared/tracer_driver/tropchem/moz.mods.F90 mpp.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_shared/tracer_driver/tropchem/moz.mods.F90
moz.subs.o: $(SRCROOT)atmos_shared/tracer_driver/tropchem/moz.subs.F90 moz.mods.o mo_jpl.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_shared/tracer_driver/tropchem/moz.subs.F90
mpp.o: $(SRCROOT)shared/mpp/mpp.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/include/fms_platform.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/system_clock.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_util.inc \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_util_sma.inc /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_util_mpi.inc /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_util_nocomm.inc                      \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_error_a_a.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_error_a_s.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_error_s_a.h                            \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_error_s_s.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_comm.inc /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_comm_sma.inc                              \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_transmit_sma.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_transmit.inc /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_reduce_sma.h                       \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_sum_sma.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_sum.inc /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_comm_mpi.inc                                 \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_transmit_mpi.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_reduce_mpi.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_sum_mpi.h                          \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_comm_nocomm.inc /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_transmit_nocomm.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_reduce_nocomm.h              \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_sum_nocomm.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_chksum_int.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_chksum_scalar.h                      \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_chksum.h mpp_parameter.o mpp_data.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/shared/include -I/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include	$(SRCROOT)shared/mpp/mpp.F90
mpp_data.o: $(SRCROOT)shared/mpp/mpp_data.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/include/fms_platform.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_data_sma.inc                                                              \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_data_mpi.inc /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_data_nocomm.inc mpp_parameter.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/shared/include -I/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include	$(SRCROOT)shared/mpp/mpp_data.F90
mpp_domains.o: $(SRCROOT)shared/mpp/mpp_domains.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/include/fms_platform.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_domains_util.inc                                                    \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_domains_comm.inc /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_domains_define.inc /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_domains_misc.inc           \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_update_domains2D.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_do_update.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_do_updateV.h                    \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_do_check.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_do_checkV.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_do_redistribute.h                       \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_get_boundary.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_do_get_boundary.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_domains_reduce.inc            \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_global_reduce.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_global_sum.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_global_sum_tl.h                   \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_global_field.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_do_global_field.h mpp_parameter.o mpp_data.o mpp.o mpp_memutils.o mpp_pset.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/shared/include -I/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include	$(SRCROOT)shared/mpp/mpp_domains.F90
mpp_io.o: $(SRCROOT)shared/mpp/mpp_io.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/include/fms_platform.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_io_util.inc                                                                   \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_io_misc.inc /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_io_connect.inc /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_io_read.inc                         \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_read_2Ddecomp.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_io_write.inc /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_write_2Ddecomp.h                  \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_write.h mpp_parameter.o mpp.o mpp_domains.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/shared/include -I/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include	$(SRCROOT)shared/mpp/mpp_io.F90
mpp_memutils.o: $(SRCROOT)shared/mpp/mpp_memutils.F90 mpp.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)shared/mpp/mpp_memutils.F90
mpp_parameter.o: $(SRCROOT)shared/mpp/mpp_parameter.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/include/fms_platform.h
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/shared/include	$(SRCROOT)shared/mpp/mpp_parameter.F90
mpp_pset.o: $(SRCROOT)shared/mpp/mpp_pset.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/include/fms_platform.h mpp.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/shared/include	$(SRCROOT)shared/mpp/mpp_pset.F90
mpp_utilities.o: $(SRCROOT)shared/mpp/mpp_utilities.F90 mpp.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)shared/mpp/mpp_utilities.F90
mrgrnk.o: $(SRCROOT)atmos_param/cosp/quickbeam/mrgrnk.f90
	$(FC) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/cosp/quickbeam/mrgrnk.f90
my25_turb.o: $(SRCROOT)atmos_param/my25_turb/my25_turb.F90 fms.o fms_io.o tridiagonal.o constants.o monin_obukhov.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/my25_turb/my25_turb.F90
nonfms_donner.o: $(SRCROOT)atmos_param/donner_deep/nonfms_donner.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/atmos_param/donner_deep/donner_nml.h sat_vapor_pres_k.o donner_types.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/atmos_param/donner_deep	$(SRCROOT)atmos_param/donner_deep/nonfms_donner.F90
nsclock.o: $(SRCROOT)shared/mpp/nsclock.c
	$(CC) $(CPPDEFS) $(CPPFLAGS) $(CFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)shared/mpp/nsclock.c
numerics.o: $(SRCROOT)land_lad/numerics.F90 fms.o constants.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)land_lad/numerics.F90
ocean_adv_vel_diag.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_diag/ocean_adv_vel_diag.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_memory.h constants.o diag_manager.o fms.o mpp.o time_manager.o ocean_domains.o        \
ocean_operators.o ocean_parameters.o ocean_types.o ocean_util.o ocean_workspace.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_diag/ocean_adv_vel_diag.F90
ocean_advection_velocity.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_advection_velocity.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_memory.h axis_utils.o constants.o diag_manager.o fms.o mpp_domains.o      \
mpp.o ocean_domains.o ocean_operators.o ocean_parameters.o ocean_types.o ocean_workspace.o ocean_obc.o ocean_util.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_advection_velocity.F90
ocean_age_tracer.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_age_tracer.F90 field_manager.o mpp.o time_manager.o ocean_tpm_util.o fm_util.o ocean_types.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_age_tracer.F90
ocean_albedo.o: /home/wenchang/scratch/tiger3/MOM4.1/src/ice_param/ocean_albedo.F90 fms.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	/home/wenchang/scratch/tiger3/MOM4.1/src/ice_param/ocean_albedo.F90
ocean_barotropic.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_barotropic.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_memory.h constants.o diag_manager.o fms.o fms_io.o mpp_domains.o mpp.o time_manager.o     \
ocean_bih_friction.o ocean_domains.o ocean_lap_friction.o ocean_obc.o ocean_operators.o ocean_parameters.o ocean_types.o ocean_util.o ocean_workspace.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_barotropic.F90
ocean_bbc.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_bbc.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_memory.h diag_manager.o fms.o mpp.o mpp_domains.o ocean_parameters.o ocean_types.o ocean_domains.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_bbc.F90
ocean_bgc_restore.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_bgc/ocean_bgc_restore.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/include/fms_platform.h time_manager.o diag_manager.o field_manager.o fms.o fms_io.o mpp.o                 \
time_interp_external.o mpp_domains.o constants.o ocean_tpm_util.o fm_util.o coupler_types.o ocean_types.o ocmip2_co2calc.o atmos_ocean_fluxes.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/shared/include	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_bgc/ocean_bgc_restore.F90
ocean_bih_friction.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_bih_friction.F90 constants.o diag_manager.o fms.o fms_io.o mpp_domains.o mpp.o ocean_bihcst_friction.o ocean_bihgen_friction.o ocean_domains.o                  \
ocean_operators.o ocean_parameters.o ocean_types.o ocean_util.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_bih_friction.F90
ocean_bih_tracer.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_bih_tracer.F90 constants.o diag_manager.o fms.o mpp_domains.o mpp.o ocean_domains.o ocean_operators.o ocean_obc.o ocean_parameters.o ocean_types.o                \
ocean_workspace.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_bih_tracer.F90
ocean_bihcst_friction.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_bihcst_friction.F90 constants.o diag_manager.o fms.o mpp_domains.o mpp.o ocean_domains.o ocean_obc.o ocean_operators.o ocean_parameters.o ocean_types.o      \
ocean_util.o ocean_workspace.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_bihcst_friction.F90
ocean_bihgen_friction.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_bihgen_friction.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_memory.h constants.o diag_manager.o fms.o mpp_domains.o mpp.o           \
ocean_domains.o ocean_obc.o ocean_operators.o ocean_parameters.o ocean_types.o ocean_util.o ocean_workspace.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_bihgen_friction.F90
ocean_convect.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_convect.F90 diag_manager.o fms.o ocean_density.o ocean_domains.o ocean_parameters.o ocean_types.o ocean_workspace.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_convect.F90
ocean_coriolis.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_coriolis.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_memory.h constants.o diag_manager.o fms.o mpp.o ocean_domains.o ocean_parameters.o            \
ocean_types.o ocean_util.o ocean_workspace.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_coriolis.F90
ocean_density.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_density.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/include/fms_platform.h /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_memory.h constants.o     \
diag_manager.o fms.o fms_io.o mpp_domains.o mpp.o platform.o time_manager.o field_manager.o ocean_domains.o ocean_parameters.o ocean_pressure.o ocean_types.o ocean_util.o ocean_workspace.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/shared/include -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_density.F90
ocean_diagnostics.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_diag/ocean_diagnostics.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_memory.h diag_manager.o fms.o mpp.o time_manager.o ocean_adv_vel_diag.o ocean_domains.o \
ocean_tracer_diag.o ocean_types.o ocean_velocity_diag.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_diag/ocean_diagnostics.F90
ocean_domains.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_domains.F90 fms.o mpp_domains.o mpp.o ocean_types.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_domains.F90
ocean_drifters.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_diag/ocean_drifters.F90 drifters.o fms.o mpp_domains.o time_manager.o ocean_domains.o ocean_parameters.o ocean_types.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_diag/ocean_drifters.F90
ocean_form_drag.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_form_drag.F90 constants.o diag_manager.o fms.o mpp.o mpp_domains.o ocean_domains.o ocean_parameters.o ocean_types.o ocean_workspace.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_form_drag.F90
ocean_frazil.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_frazil.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_memory.h constants.o diag_manager.o fms.o mpp.o ocean_domains.o ocean_parameters.o             \
ocean_tpm_util.o ocean_types.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_frazil.F90
ocean_generic_tracer.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_bgc/ocean_generic_tracer.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/include/fms_platform.h ocean_tpm_util.o ocean_types.o ocean_parameters.o mpp.o field_manager.o      \
generic_tracer.o generic_tracer_utils.o coupler_types.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/shared/include	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_bgc/ocean_generic_tracer.F90
ocean_grids.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_grids.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_memory.h constants.o diag_manager.o fms.o mpp_domains.o mpp.o mosaic.o ocean_domains.o              \
ocean_parameters.o ocean_types.o ocean_workspace.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_grids.F90
ocean_ibgc.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_bgc/ocean_ibgc.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/include/fms_platform.h diag_manager.o field_manager.o mpp.o fms.o fms_io.o time_manager.o time_interp_external.o        \
mpp_domains.o constants.o ocean_tpm_util.o fm_util.o ocean_types.o ocmip2_co2calc.o coupler_types.o atmos_ocean_fluxes.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/shared/include	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_bgc/ocean_ibgc.F90
ocean_increment_eta.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_increment_eta.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_memory.h diag_manager.o fms.o mpp.o time_interp_external.o time_manager.o  \
ocean_domains.o ocean_parameters.o ocean_types.o ocean_workspace.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_increment_eta.F90
ocean_increment_tracer.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_increment_tracer.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_memory.h diag_manager.o fms.o mpp.o time_interp_external.o           \
time_manager.o ocean_domains.o ocean_parameters.o ocean_types.o ocean_workspace.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_increment_tracer.F90
ocean_increment_velocity.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_increment_velocity.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_memory.h diag_manager.o fms.o mpp.o time_interp_external.o       \
time_manager.o ocean_domains.o ocean_parameters.o ocean_types.o ocean_workspace.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_increment_velocity.F90
ocean_lap_friction.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_lap_friction.F90 diag_manager.o fms.o fms_io.o mpp_domains.o mpp.o ocean_domains.o ocean_lapcst_friction.o ocean_lapgen_friction.o ocean_operators.o            \
ocean_parameters.o ocean_types.o ocean_util.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_lap_friction.F90
ocean_lap_tracer.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_lap_tracer.F90 constants.o diag_manager.o fms.o mpp_domains.o mpp.o ocean_domains.o ocean_obc.o ocean_operators.o ocean_parameters.o ocean_types.o                \
ocean_workspace.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_lap_tracer.F90
ocean_lapcst_friction.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_lapcst_friction.F90 constants.o diag_manager.o fms.o mpp_domains.o mpp.o ocean_domains.o ocean_obc.o ocean_operators.o ocean_parameters.o ocean_types.o      \
ocean_util.o ocean_workspace.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_lapcst_friction.F90
ocean_lapgen_friction.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_lapgen_friction.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_memory.h constants.o diag_manager.o fms.o mpp_domains.o mpp.o           \
ocean_domains.o ocean_obc.o ocean_operators.o ocean_parameters.o ocean_types.o ocean_util.o ocean_workspace.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_lapgen_friction.F90
ocean_mixdownslope.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_mixdownslope.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_memory.h constants.o diag_manager.o fms.o mpp_domains.o mpp.o ocean_density.o \
ocean_domains.o ocean_parameters.o ocean_types.o ocean_util.o ocean_workspace.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_mixdownslope.F90
ocean_model.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_model.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_memory.h fms.o fms_io.o mpp_domains.o mpp.o stock_constants.o time_interp_external.o time_manager.o \
ocean_advection_velocity.o ocean_barotropic.o ocean_bbc.o ocean_bih_friction.o ocean_convect.o ocean_coriolis.o ocean_density.o ocean_diagnostics.o ocean_domains.o ocean_form_drag.o ocean_grids.o ocean_increment_eta.o ocean_increment_tracer.o             \
ocean_increment_velocity.o ocean_lap_tracer.o ocean_bih_tracer.o ocean_lap_friction.o ocean_mixdownslope.o ocean_momentum_source.o ocean_nphysics.o ocean_obc.o ocean_operators.o ocean_overexchange.o ocean_overflow.o ocean_passive.o ocean_polar_filter.o   \
ocean_pressure.o ocean_rivermix.o ocean_riverspread.o ocean_parameters.o ocean_sbc.o ocean_shortwave.o ocean_sigma_transport.o ocean_sponges_eta.o ocean_sponges_tracer.o ocean_sponges_velocity.o ocean_submesoscale.o ocean_tempsalt.o ocean_thickness.o     \
ocean_time_filter.o ocean_topog.o ocean_tracer_advect.o ocean_tracer.o ocean_tracer_util.o ocean_tpm.o ocean_types.o ocean_util.o ocean_velocity_advect.o ocean_velocity_diag.o ocean_velocity.o ocean_vert_mix.o ocean_vert_gotm.o ocean_workspace.o          \
ocean_xlandinsert.o ocean_xlandmix.o ocean_drifters.o oda_driver.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_model.F90
ocean_momentum_source.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_momentum_source.F90 constants.o diag_manager.o field_manager.o fms.o mpp_domains.o mpp.o ocean_domains.o ocean_parameters.o ocean_types.o ocean_workspace.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_momentum_source.F90
ocean_nphysics.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_nphysics.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_memory.h constants.o diag_manager.o fms.o mpp.o mpp_domains.o ocean_domains.o         \
ocean_nphysics_util.o ocean_nphysicsA.o ocean_nphysicsB.o ocean_nphysicsC.o ocean_parameters.o ocean_types.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_nphysics.F90
ocean_nphysicsA.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_nphysicsA.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_memory.h constants.o diag_manager.o fms.o mpp_domains.o mpp.o time_manager.o        \
ocean_domains.o ocean_nphysics_util.o ocean_operators.o ocean_parameters.o ocean_sigma_transport.o ocean_types.o ocean_util.o ocean_workspace.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_nphysicsA.F90
ocean_nphysicsB.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_nphysicsB.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_memory.h constants.o diag_manager.o fms.o fms_io.o mpp_domains.o mpp.o              \
time_manager.o ocean_domains.o ocean_nphysics_util.o ocean_operators.o ocean_parameters.o ocean_sigma_transport.o ocean_types.o ocean_util.o ocean_workspace.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_nphysicsB.F90
ocean_nphysicsC.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_nphysicsC.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_memory.h constants.o diag_manager.o fms.o fms_io.o mpp_domains.o mpp.o              \
time_manager.o ocean_domains.o ocean_nphysics_util.o ocean_operators.o ocean_parameters.o ocean_types.o ocean_util.o ocean_workspace.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_nphysicsC.F90
ocean_nphysics_util.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_nphysics_util.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_memory.h constants.o diag_manager.o fms.o fms_io.o mpp.o mpp_domains.o      \
time_manager.o ocean_domains.o ocean_operators.o ocean_parameters.o ocean_tracer_diag.o ocean_types.o ocean_util.o ocean_workspace.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_nphysics_util.F90
ocean_obc.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_obc.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/include/fms_platform.h constants.o data_override.o diag_manager.o fms.o fms_io.o mpp_io.o mpp_domains.o mpp.o            \
time_interp_external.o time_manager.o tracer_manager.o ocean_util.o ocean_domains.o ocean_parameters.o ocean_types.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/shared/include	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_obc.F90
ocean_operators.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_operators.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_memory.h mpp_domains.o mpp.o ocean_domains.o ocean_parameters.o ocean_types.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_operators.F90
ocean_overexchange.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_overexchange.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_memory.h constants.o diag_manager.o fms.o mpp_domains.o mpp.o                \
ocean_density.o ocean_domains.o ocean_parameters.o ocean_types.o ocean_util.o ocean_workspace.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_overexchange.F90
ocean_overflow.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_overflow.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_memory.h constants.o diag_manager.o fms.o mpp_domains.o mpp.o ocean_density.o        \
ocean_domains.o ocean_parameters.o ocean_types.o ocean_util.o ocean_workspace.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_overflow.F90
ocean_parameters.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_parameters.F90
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_parameters.F90
ocean_passive.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_passive.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_memory.h constants.o field_manager.o fm_util.o fms.o mpp.o ocean_domains.o ocean_tpm_util.o  \
ocean_types.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_passive.F90
ocean_pert_co2.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_bgc/ocean_pert_co2.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/include/fms_platform.h time_manager.o diag_manager.o field_manager.o fms.o mpp.o mpp_domains.o constants.o      \
ocean_tpm_util.o fm_util.o coupler_types.o ocean_types.o ocmip2_co2calc.o atmos_ocean_fluxes.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/shared/include	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_bgc/ocean_pert_co2.F90
ocean_po4_pre.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_bgc/ocean_po4_pre.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/include/fms_platform.h field_manager.o mpp.o fms.o time_manager.o mpp_domains.o ocean_tpm_util.o fm_util.o        \
ocean_types.o ocean_tracer_diag.o diag_manager.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/shared/include	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_bgc/ocean_po4_pre.F90
ocean_polar_filter.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_polar_filter.F90 axis_utils.o constants.o diag_manager.o fms.o mpp_domains.o mpp.o ocean_domains.o ocean_parameters.o ocean_types.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_polar_filter.F90
ocean_pressure.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_pressure.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_memory.h constants.o diag_manager.o fms.o mpp_io.o mpp.o ocean_domains.o ocean_operators.o    \
ocean_parameters.o ocean_types.o ocean_util.o ocean_workspace.o ocean_obc.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_pressure.F90
ocean_residency.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_residency.F90 time_manager.o field_manager.o mpp.o diag_manager.o ocean_tpm_util.o fm_util.o ocean_types.o ocean_residency_meta.o ocean_residency_ml.o                  \
ocean_residency_range.o ocean_residency_integrand.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_residency.F90
ocean_residency_integrand.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_residency_integrand.F90 field_manager.o mpp.o fms.o ocean_residency_meta.o ocean_types.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_residency_integrand.F90
ocean_residency_meta.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_residency_meta.F90 field_manager.o fm_util.o mpp.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_residency_meta.F90
ocean_residency_ml.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_residency_ml.F90 field_manager.o mpp.o ocean_residency_meta.o ocean_types.o ocean_tracer_diag.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_residency_ml.F90
ocean_residency_range.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_residency_range.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/include/fms_platform.h field_manager.o mpp.o ocean_residency_meta.o ocean_types.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/shared/include	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_residency_range.F90
ocean_rivermix.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_rivermix.F90 axis_utils.o constants.o diag_manager.o fms.o mpp_domains.o mpp.o ocean_domains.o ocean_parameters.o ocean_types.o ocean_workspace.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_rivermix.F90
ocean_riverspread.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_riverspread.F90 field_manager.o fms.o mpp_domains.o mpp.o ocean_domains.o ocean_types.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_riverspread.F90
ocean_rough.o: /home/wenchang/scratch/tiger3/MOM4.1/src/ice_param/ocean_rough.F90 fms.o constants.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	/home/wenchang/scratch/tiger3/MOM4.1/src/ice_param/ocean_rough.F90
ocean_sbc.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_sbc.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/include/fms_platform.h /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_memory.h constants.o             \
diag_manager.o fms.o fms_io.o mpp_domains.o mpp.o time_interp_external.o time_manager.o ocean_domains.o ocean_parameters.o ocean_riverspread.o ocean_tpm.o ocean_types.o ocean_workspace.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/shared/include -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_sbc.F90
ocean_shortwave.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_shortwave.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/include/fms_platform.h /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_memory.h    \
constants.o diag_manager.o fms.o mpp.o ocean_domains.o ocean_parameters.o ocean_shortwave_csiro.o ocean_shortwave_jerlov.o ocean_shortwave_gfdl.o ocean_types.o ocean_tpm_util.o ocean_workspace.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/shared/include -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_shortwave.F90
ocean_shortwave_csiro.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_shortwave_csiro.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_memory.h axis_utils.o field_manager.o fms.o mpp.o                      \
time_interp_external.o ocean_domains.o ocean_types.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_shortwave_csiro.F90
ocean_shortwave_gfdl.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_shortwave_gfdl.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_memory.h axis_utils.o constants.o diag_manager.o field_manager.o fms.o   \
mpp.o time_interp_external.o ocean_domains.o ocean_parameters.o ocean_types.o ocean_workspace.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_shortwave_gfdl.F90
ocean_shortwave_jerlov.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_shortwave_jerlov.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_memory.h constants.o fms.o mpp.o time_interp_external.o              \
ocean_domains.o ocean_parameters.o ocean_types.o ocean_workspace.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_shortwave_jerlov.F90
ocean_sigma_transport.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_sigma_transport.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_memory.h constants.o diag_manager.o fms.o fms_io.o mpp_domains.o mpp.o  \
ocean_domains.o ocean_density.o ocean_operators.o ocean_parameters.o ocean_types.o ocean_util.o ocean_workspace.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_sigma_transport.F90
ocean_sponges_eta.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_sponges_eta.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_memory.h diag_manager.o fms.o mpp.o time_interp_external.o time_manager.o      \
ocean_domains.o ocean_parameters.o ocean_types.o ocean_workspace.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_sponges_eta.F90
ocean_sponges_tracer.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_sponges_tracer.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_memory.h diag_manager.o fms.o mpp.o time_interp_external.o               \
time_manager.o ocean_domains.o ocean_parameters.o ocean_types.o ocean_workspace.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_sponges_tracer.F90
ocean_sponges_velocity.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_sponges_velocity.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_memory.h diag_manager.o fms.o mpp.o time_interp_external.o           \
time_manager.o ocean_domains.o ocean_parameters.o ocean_types.o ocean_workspace.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_sponges_velocity.F90
ocean_submesoscale.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_submesoscale.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_memory.h constants.o diag_manager.o fms.o mpp_domains.o mpp.o ocean_domains.o \
ocean_operators.o ocean_parameters.o ocean_tracer_diag.o ocean_types.o ocean_util.o ocean_workspace.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_submesoscale.F90
ocean_tempsalt.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_tempsalt.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_memory.h constants.o fms.o mpp.o ocean_domains.o ocean_parameters.o ocean_tpm_util.o       \
ocean_types.o ocean_workspace.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_tempsalt.F90
ocean_thickness.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_thickness.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_memory.h constants.o diag_manager.o fms.o fms_io.o mpp_domains.o mpp.o ocean_domains.o      \
ocean_grids.o ocean_parameters.o ocean_tracer_util.o ocean_types.o ocean_util.o ocean_workspace.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_thickness.F90
ocean_time_filter.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_time_filter.F90 constants.o diag_manager.o fms.o mpp_domains.o mpp.o ocean_domains.o ocean_operators.o ocean_parameters.o ocean_types.o ocean_velocity_diag.o   \
ocean_workspace.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_time_filter.F90
ocean_topog.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_topog.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_memory.h constants.o fms.o mpp_domains.o mpp.o axis_utils.o ocean_domains.o ocean_parameters.o      \
ocean_types.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_topog.F90
ocean_tpm.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_tpm.F90 mpp.o mpp_domains.o ocean_types.o ocean_age_tracer.o ocean_residency.o ocean_pert_co2.o ocmip2_abiotic.o ocmip2_cfc.o ocmip2_biotic.o ocean_bgc_restore.o ocmip2_he.o \
ocean_po4_pre.o ocean_ibgc.o ocean_generic_tracer.o ocean_frazil.o ocean_tempsalt.o ocean_passive.o transport_matrix.o time_manager.o coupler_types.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_tpm.F90
ocean_tpm_util.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_tpm_util.F90 field_manager.o fms.o mpp.o fm_util.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_tpm_util.F90
ocean_tracer.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_tracer.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_memory.h constants.o diag_manager.o field_manager.o fms.o fms_io.o fm_util.o mpp_domains.o     \
mpp_io.o mpp.o platform.o time_manager.o transport_matrix.o ocean_convect.o ocean_domains.o ocean_frazil.o ocean_bih_tracer.o ocean_generic_tracer.o ocean_lap_tracer.o ocean_obc.o ocean_parameters.o ocean_passive.o ocean_polar_filter.o ocean_shortwave.o  \
ocean_tempsalt.o ocean_tpm.o ocean_tpm_util.o ocean_tracer_advect.o ocean_tracer_util.o ocean_types.o ocean_util.o ocean_vert_mix.o ocean_workspace.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_tracer.F90
ocean_tracer_advect.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_tracer_advect.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_memory.h constants.o diag_manager.o fms.o fms_io.o mpp_domains.o mpp.o           \
ocean_domains.o ocean_obc.o ocean_parameters.o ocean_topog.o ocean_tracer_util.o ocean_types.o ocean_workspace.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_tracer_advect.F90
ocean_tracer_diag.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_diag/ocean_tracer_diag.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_memory.h constants.o diag_manager.o fms.o mpp_domains.o mpp.o time_manager.o            \
ocean_density.o ocean_domains.o ocean_obc.o ocean_operators.o ocean_parameters.o ocean_tracer_util.o ocean_types.o ocean_util.o ocean_workspace.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_diag/ocean_tracer_diag.F90
ocean_tracer_util.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_diag/ocean_tracer_util.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_memory.h mpp.o platform.o ocean_domains.o ocean_parameters.o ocean_types.o ocean_util.o \
ocean_workspace.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_diag/ocean_tracer_util.F90
ocean_types.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_types.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/include/fms_platform.h /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_memory.h coupler_types.o     \
field_manager.o fms.o mpp_domains.o mpp.o time_manager.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/shared/include -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_types.F90
ocean_util.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_util.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_memory.h constants.o mpp_domains.o mpp.o time_manager.o ocean_domains.o ocean_types.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_util.F90
ocean_velocity.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_velocity.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_memory.h constants.o diag_manager.o fms.o fms_io.o mpp_domains.o mpp.o ocean_bih_friction.o   \
ocean_coriolis.o ocean_domains.o ocean_form_drag.o ocean_lap_friction.o ocean_momentum_source.o ocean_obc.o ocean_operators.o ocean_parameters.o ocean_pressure.o ocean_types.o ocean_util.o ocean_velocity_advect.o ocean_velocity_diag.o ocean_vert_mix.o    \
ocean_workspace.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_velocity.F90
ocean_velocity_advect.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_velocity_advect.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_memory.h diag_manager.o fms.o mpp.o ocean_domains.o ocean_obc.o                 \
ocean_operators.o ocean_parameters.o ocean_types.o ocean_workspace.o ocean_util.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_velocity_advect.F90
ocean_velocity_diag.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_diag/ocean_velocity_diag.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/include/fms_platform.h /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_memory.h     \
constants.o diag_manager.o fms.o mpp_domains.o mpp.o time_manager.o ocean_bih_friction.o ocean_coriolis.o ocean_domains.o ocean_form_drag.o ocean_lap_friction.o ocean_momentum_source.o ocean_operators.o ocean_parameters.o ocean_pressure.o ocean_types.o   \
ocean_util.o ocean_velocity_advect.o ocean_vert_mix.o ocean_workspace.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/shared/include -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_diag/ocean_velocity_diag.F90
ocean_vert_chen.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_vert_chen.F90 constants.o diag_manager.o fms.o fms_io.o mpp_domains.o mpp.o ocean_density.o ocean_domains.o ocean_parameters.o ocean_shortwave_csiro.o             \
ocean_types.o ocean_util.o ocean_workspace.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_vert_chen.F90
ocean_vert_const.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_vert_const.F90 constants.o diag_manager.o fms.o mpp_io.o mpp.o ocean_density.o ocean_domains.o ocean_parameters.o ocean_types.o ocean_workspace.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_vert_const.F90
ocean_vert_gotm.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_vert_gotm.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_memory.h constants.o diag_manager.o fms.o fms_io.o mpp_domains.o mpp.o              \
tridiagonal_gotm.o turbulence.o ocean_domains.o ocean_parameters.o ocean_types.o ocean_util.o ocean_workspace.o ocean_obc.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_vert_gotm.F90
ocean_vert_kpp.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_vert_kpp.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_memory.h constants.o diag_manager.o fms.o mpp_domains.o mpp.o ocean_density.o         \
ocean_domains.o ocean_parameters.o ocean_types.o ocean_workspace.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_vert_kpp.F90
ocean_vert_kpp_mom4p0.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_vert_kpp_mom4p0.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_memory.h constants.o diag_manager.o fms.o mpp_domains.o mpp.o           \
ocean_density.o ocean_domains.o ocean_parameters.o ocean_types.o ocean_workspace.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_vert_kpp_mom4p0.F90
ocean_vert_mix.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_vert_mix.F90 constants.o diag_manager.o field_manager.o fms.o mpp.o ocean_domains.o ocean_parameters.o ocean_tracer_util.o ocean_types.o ocean_util.o               \
ocean_vert_const.o ocean_vert_chen.o ocean_vert_gotm.o ocean_vert_kpp.o ocean_vert_kpp_mom4p0.o ocean_vert_pp.o ocean_vert_tidal.o ocean_workspace.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_vert_mix.F90
ocean_vert_pp.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_vert_pp.F90 constants.o diag_manager.o fms.o mpp.o ocean_density.o ocean_domains.o ocean_parameters.o ocean_types.o ocean_workspace.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_vert_pp.F90
ocean_vert_tidal.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_vert_tidal.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_memory.h constants.o diag_manager.o fms.o mpp_domains.o mpp.o ocean_domains.o     \
ocean_operators.o ocean_parameters.o ocean_types.o ocean_workspace.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_vert_tidal.F90
ocean_workspace.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_workspace.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_memory.h ocean_types.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_workspace.F90
ocean_xlandinsert.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_xlandinsert.F90 constants.o diag_manager.o field_manager.o fms.o mpp_domains.o mpp.o ocean_domains.o ocean_parameters.o ocean_types.o ocean_workspace.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_xlandinsert.F90
ocean_xlandmix.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_xlandmix.F90 constants.o diag_manager.o field_manager.o fms.o mpp_domains.o mpp.o ocean_domains.o ocean_parameters.o ocean_types.o ocean_workspace.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_xlandmix.F90
ocmip2_abiotic.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_bgc/ocmip2_abiotic.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/include/fms_platform.h time_manager.o diag_manager.o field_manager.o fms.o fms_io.o mpp.o                       \
time_interp_external.o mpp_domains.o constants.o ocean_tpm_util.o fm_util.o coupler_types.o ocean_types.o ocmip2_co2calc.o atmos_ocean_fluxes.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/shared/include	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_bgc/ocmip2_abiotic.F90
ocmip2_biotic.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_bgc/ocmip2_biotic.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/include/fms_platform.h time_manager.o diag_manager.o field_manager.o fms.o fms_io.o mpp.o time_interp_external.o  \
mpp_domains.o constants.o ocean_tpm_util.o fm_util.o coupler_types.o ocean_types.o ocmip2_co2calc.o atmos_ocean_fluxes.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/shared/include	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_bgc/ocmip2_biotic.F90
ocmip2_cfc.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_bgc/ocmip2_cfc.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/include/fms_platform.h time_manager.o diag_manager.o field_manager.o fms.o ocean_tpm_util.o constants.o fm_util.o mpp.o \
coupler_types.o ocean_types.o atmos_ocean_fluxes.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/shared/include	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_bgc/ocmip2_cfc.F90
ocmip2_co2calc.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_bgc/ocmip2_co2calc.F90
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_bgc/ocmip2_co2calc.F90
ocmip2_he.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_bgc/ocmip2_he.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/include/fms_platform.h time_manager.o time_interp_external.o diag_manager.o field_manager.o fms.o fms_io.o                \
ocean_tpm_util.o fm_util.o mpp.o coupler_types.o ocean_types.o mpp_domains.o atmos_ocean_fluxes.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/shared/include	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_bgc/ocmip2_he.F90
oda_core.o: $(SRCROOT)shared/oda_tools/oda_core.F90 fms.o mpp.o mpp_domains.o time_manager.o get_cal_time.o axis_utils.o constants.o oda_types.o write_ocean_data.o mpp_io.o field_manager.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)shared/oda_tools/oda_core.F90
oda_driver.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/oda_driver.F90 ocean_types.o oda_types.o oda_core.o mpp_domains.o mpp.o mpp_io.o time_manager.o ocean_grids.o ocean_topog.o ocean_convect.o ocean_domains.o constants.o               \
ocean_workspace.o write_ocean_data.o ensemble_manager.o fms.o diag_manager.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/oda_driver.F90
oda_types.o: $(SRCROOT)shared/oda_tools/oda_types.F90 time_manager.o mpp.o mpp_domains.o fms.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)shared/oda_tools/oda_types.F90
ode_solvers.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/ode_solvers.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/cppdefs.h                                                                \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/version.h
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/ode_solvers.F90
optical_path.o: $(SRCROOT)atmos_param/sea_esf_rad/optical_path.F90 fms.o constants.o rad_utilities.o longwave_params.o lw_gases_stdtf.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/sea_esf_rad/optical_path.F90
optics_lib.o: $(SRCROOT)atmos_param/cosp/quickbeam/optics_lib.f90
	$(FC) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/cosp/quickbeam/optics_lib.f90
original_fms_rad.o: $(SRCROOT)atmos_param/sea_esf_rad/original_fms_rad.F90 mcm_lw.o mcm_sw_driver.o fsrad.o clouds.o time_manager.o fms.o rad_utilities.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/sea_esf_rad/original_fms_rad.F90
ozone.o: $(SRCROOT)atmos_param/sea_esf_rad/ozone.F90 fms.o fms_io.o time_manager.o diag_manager.o time_interp.o constants.o interpolator.o tracer_manager.o field_manager.o rad_utilities.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/sea_esf_rad/ozone.F90
par_vecsum.o: $(SRCROOT)atmos_fv_dynamics/tools/par_vecsum.F90 mod_comm.o fv_arrays.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_fv_dynamics/tools/par_vecsum.F90
pf_to_mr.o: $(SRCROOT)atmos_param/cosp/llnl/pf_to_mr.f
	$(FC) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/cosp/llnl/pf_to_mr.f
pft_module.o: $(SRCROOT)atmos_fv_dynamics/model/pft_module.F90 ecmfft.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_fv_dynamics/model/pft_module.F90
physics_driver.o: $(SRCROOT)atmos_param/physics_driver/physics_driver.F90 time_manager.o field_manager.o tracer_manager.o atmos_tracer_driver.o fms.o fms_io.o constants.o diag_manager.o rad_utilities.o cosp_driver.o moist_processes.o moistproc_kernels.o  \
vert_turb_driver.o vert_diff_driver.o radiation_driver.o cloud_spec.o aerosol.o radiative_gases.o damping_driver.o grey_radiation.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/physics_driver/physics_driver.F90
platform.o: $(SRCROOT)shared/platform/platform.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/include/fms_platform.h
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/shared/include	$(SRCROOT)shared/platform/platform.F90
pmaxmin.o: $(SRCROOT)atmos_fv_dynamics/tools/pmaxmin.F90 mod_comm.o fv_arrays.o mpp.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_fv_dynamics/tools/pmaxmin.F90
potentialml.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/potentialml.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/cppdefs.h                                                          \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/version.h turbulence.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/potentialml.F90
prec_scops.o: $(SRCROOT)atmos_param/cosp/llnl/prec_scops.f
	$(FC) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/cosp/llnl/prec_scops.f
production.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/production.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/cppdefs.h                                                            \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/version.h turbulence.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/production.F90
pv_module.o: $(SRCROOT)atmos_fv_dynamics/tools/pv_module.F90 fv_pack.o mod_comm.o fv_arrays.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_fv_dynamics/tools/pv_module.F90
q2over2eq.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/q2over2eq.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/cppdefs.h                                                              \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/version.h turbulence.o util.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/q2over2eq.F90
quicksort.o: $(SRCROOT)shared/drifters/quicksort.F90
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)shared/drifters/quicksort.F90
r_ratio.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/r_ratio.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/cppdefs.h                                                                  \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/version.h turbulence.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/r_ratio.F90
rad_diag.o: $(SRCROOT)atmos_param/fsrad/rad_diag.F90 rdparm.o hconst.o longwave.o fms.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/fsrad/rad_diag.F90
rad_output_file.o: $(SRCROOT)atmos_param/sea_esf_rad/rad_output_file.F90 fms.o time_manager.o diag_manager.o constants.o rad_utilities.o esfsw_parameters.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/sea_esf_rad/rad_output_file.F90
rad_utilities.o: $(SRCROOT)atmos_param/sea_esf_rad/rad_utilities.F90 fms.o field_manager.o time_manager.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/sea_esf_rad/rad_utilities.F90
radar_simulator.o: $(SRCROOT)atmos_param/cosp/quickbeam/radar_simulator.f90 mrgrnk.o array_lib.o math_lib.o optics_lib.o radar_simulator_types.o
	$(FC) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/cosp/quickbeam/radar_simulator.f90
radar_simulator_types.o: $(SRCROOT)atmos_param/cosp/quickbeam/radar_simulator_types.f90
	$(FC) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/cosp/quickbeam/radar_simulator_types.f90
radiation_diag.o: $(SRCROOT)atmos_param/sea_esf_rad/radiation_diag.F90 fms.o constants.o rad_utilities.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/sea_esf_rad/radiation_diag.F90
radiation_driver.o: $(SRCROOT)atmos_param/radiation_driver/radiation_driver.F90 fms.o fms_io.o diag_manager.o time_manager.o sat_vapor_pres.o constants.o data_override.o rad_utilities.o esfsw_parameters.o diag_integral.o astronomy.o original_fms_rad.o    \
sea_esf_rad.o rad_output_file.o cloudrad_package.o cloudrad_diagnostics.o microphys_rad.o aerosolrad_package.o field_manager.o tracer_manager.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/radiation_driver/radiation_driver.F90
radiative_gases.o: $(SRCROOT)atmos_param/sea_esf_rad/radiative_gases.F90 time_manager.o diag_manager.o fms.o fms_io.o time_interp.o tracer_manager.o field_manager.o rad_utilities.o ozone.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/sea_esf_rad/radiative_gases.F90
random_numbers.o: $(SRCROOT)shared/random_numbers/random_numbers.F90 MersenneTwister.o time_manager.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)shared/random_numbers/random_numbers.F90
ras.o: $(SRCROOT)atmos_param/ras/ras.F90 mpp.o sat_vapor_pres.o constants.o diag_manager.o time_manager.o fms.o field_manager.o tracer_manager.o rad_utilities.o aer_ccn_act.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/ras/ras.F90
rdparm.o: $(SRCROOT)atmos_param/fsrad/rdparm.F90 fms.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/fsrad/rdparm.F90
read_mosaic.o: $(SRCROOT)shared/mosaic/read_mosaic.c /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mosaic/read_mosaic.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mosaic/constant.h                                                                    \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mosaic/mosaic_util.h
	$(CC) $(CPPDEFS) $(CPPFLAGS) $(CFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mosaic	$(SRCROOT)shared/mosaic/read_mosaic.c
rh_based_clouds.o: $(SRCROOT)atmos_param/sea_esf_rad/rh_based_clouds.F90 fms.o rh_clouds.o rad_utilities.o constants.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/sea_esf_rad/rh_based_clouds.F90
rh_clouds.o: $(SRCROOT)atmos_param/rh_clouds/rh_clouds.F90 fms.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/rh_clouds/rh_clouds.F90
rivers.o: $(SRCROOT)land_lad/soil/rivers.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/include/fms_platform.h time_manager.o diag_manager.o mpp.o mpp_domains.o mpp_io.o fms.o constants.o land_types.o land_properties.o numerics.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/shared/include	$(SRCROOT)land_lad/soil/rivers.F90
rot.o: /home/wenchang/scratch/tiger3/MOM4.1/src/ice_sis/rot.F90 mpp.o axis_utils.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	/home/wenchang/scratch/tiger3/MOM4.1/src/ice_sis/rot.F90
sat_vapor_pres.o: $(SRCROOT)shared/sat_vapor_pres/sat_vapor_pres.F90 constants.o fms.o mpp_io.o sat_vapor_pres_k.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)shared/sat_vapor_pres/sat_vapor_pres.F90
sat_vapor_pres_k.o: $(SRCROOT)shared/sat_vapor_pres/sat_vapor_pres_k.F90
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)shared/sat_vapor_pres/sat_vapor_pres_k.F90
scops.o: $(SRCROOT)atmos_param/cosp/icarus-scops-3.7/scops.f /home/wenchang/scratch/tiger3/MOM4.1/src/atmos_param/cosp/icarus-scops-3.7/congvec.inc
	$(FC) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/atmos_param/cosp/icarus-scops-3.7	$(SRCROOT)atmos_param/cosp/icarus-scops-3.7/scops.f
sea_esf_rad.o: $(SRCROOT)atmos_param/sea_esf_rad/sea_esf_rad.F90 fms.o time_manager.o rad_utilities.o radiation_diag.o longwave_driver.o shortwave_driver.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/sea_esf_rad/sea_esf_rad.F90
sealw99.o: $(SRCROOT)atmos_param/sea_esf_rad/sealw99.F90 fms.o time_manager.o constants.o rad_utilities.o longwave_params.o longwave_clouds.o longwave_fluxes.o longwave_tables.o optical_path.o gas_tf.o lw_gases_stdtf.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/sea_esf_rad/sealw99.F90
set_eta.o: $(SRCROOT)atmos_fv_dynamics/tools/set_eta.F90 fv_pack.o fms.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_fv_dynamics/tools/set_eta.F90
shallow_conv.o: $(SRCROOT)atmos_param/shallow_conv/shallow_conv.F90 sat_vapor_pres.o fms.o constants.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/shallow_conv/shallow_conv.F90
shallow_physics.o: $(SRCROOT)atmos_param/shallow_physics/shallow_physics.F90 fms.o time_manager.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/shallow_physics/shallow_physics.F90
shortwave.o: $(SRCROOT)atmos_param/fsrad/shortwave.F90 rdparm.o hconst.o fms.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/fsrad/shortwave.F90
shortwave_driver.o: $(SRCROOT)atmos_param/sea_esf_rad/shortwave_driver.F90 fms.o rad_utilities.o esfsw_parameters.o lhsw_driver.o esfsw_driver.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/sea_esf_rad/shortwave_driver.F90
shr_kind_mod.o: $(SRCROOT)atmos_fv_dynamics/model/shr_kind_mod.F90
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_fv_dynamics/model/shr_kind_mod.F90
soil.o: $(SRCROOT)land_lad/soil/soil.F90 time_manager.o mpp_domains.o fms.o fms_io.o rivers.o land_types.o land_properties.o constants.o diag_manager.o data_override.o stock_constants.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)land_lad/soil/soil.F90
specified_clouds_W.o: $(SRCROOT)atmos_param/sea_esf_rad/specified_clouds_W.F90 time_manager.o cloud_zonal.o cloud_obs.o fms.o rad_utilities.o constants.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/sea_esf_rad/specified_clouds_W.F90
stable_bl_turb.o: $(SRCROOT)atmos_param/stable_bl_turb/stable_bl_turb.F90 fms.o diag_manager.o time_manager.o constants.o monin_obukhov.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/stable_bl_turb/stable_bl_turb.F90
standalone_clouds.o: $(SRCROOT)atmos_param/sea_esf_rad/standalone_clouds.F90 fms.o rad_utilities.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/sea_esf_rad/standalone_clouds.F90
station_data.o: $(SRCROOT)shared/station_data/station_data.F90 axis_utils.o mpp_io.o fms.o mpp.o mpp_domains.o diag_axis.o diag_output.o diag_manager.o diag_util.o time_manager.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)shared/station_data/station_data.F90
stock_constants.o: $(SRCROOT)shared/exchange/stock_constants.F90 mpp.o time_manager.o diag_manager.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)shared/exchange/stock_constants.F90
strat_chem_driver.o: $(SRCROOT)atmos_shared/tracer_driver/stratchem/strat_chem_driver.F90 fms.o mpp_io.o tracer_manager.o field_manager.o mpp.o constants.o strat_chem_model.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_shared/tracer_driver/stratchem/strat_chem_driver.F90
strat_chem_model.o: $(SRCROOT)atmos_shared/tracer_driver/stratchem/strat_chem_model.F90
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_shared/tracer_driver/stratchem/strat_chem_model.F90
strat_chem_utilities.o: $(SRCROOT)atmos_shared/tracer_driver/tropchem/strat_chem_utilities.F90 mpp_io.o mpp.o fms.o constants.o time_manager.o interpolator.o time_interp.o diag_manager.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_shared/tracer_driver/tropchem/strat_chem_utilities.F90
strat_cloud.o: $(SRCROOT)atmos_param/strat_cloud/strat_cloud.F90 sat_vapor_pres.o fms.o fms_io.o constants.o cloud_rad.o diag_manager.o time_manager.o cloud_generator.o betaDistribution.o rad_utilities.o aer_ccn_act.o aer_in_act.o mpp.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/strat_cloud/strat_cloud.F90
strat_clouds_W.o: $(SRCROOT)atmos_param/sea_esf_rad/strat_clouds_W.F90 constants.o time_manager.o fms.o rad_utilities.o esfsw_parameters.o cloud_rad.o random_numbers.o cloud_generator.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/sea_esf_rad/strat_clouds_W.F90
surface_flux.o: /home/wenchang/scratch/tiger3/MOM4.1/src/coupler/surface_flux.F90 fms.o monin_obukhov.o sat_vapor_pres.o constants.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	/home/wenchang/scratch/tiger3/MOM4.1/src/coupler/surface_flux.F90
sw_core.o: $(SRCROOT)atmos_fv_dynamics/model/sw_core.F90 tp_core.o shr_kind_mod.o pft_module.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_fv_dynamics/model/sw_core.F90
threadloc.o: $(SRCROOT)shared/mpp/threadloc.c
	$(CC) $(CPPDEFS) $(CPPFLAGS) $(CFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)shared/mpp/threadloc.c
time.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/time.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/cppdefs.h                                                                              \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/version.h
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/time.F90
time_interp.o: $(SRCROOT)shared/time_interp/time_interp.F90 time_manager.o fms.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)shared/time_interp/time_interp.F90
time_interp_external.o: $(SRCROOT)shared/time_interp/time_interp_external.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/include/fms_platform.h mpp.o mpp_io.o time_manager.o get_cal_time.o mpp_domains.o time_interp.o axis_utils.o fms.o platform.o    \
horiz_interp.o constants.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/shared/include	$(SRCROOT)shared/time_interp/time_interp_external.F90
time_manager.o: $(SRCROOT)shared/time_manager/time_manager.F90 constants.o fms.o fms_io.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)shared/time_manager/time_manager.F90
timingModule.o: $(SRCROOT)atmos_fv_dynamics/tools/timingModule.F90 shr_kind_mod.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_fv_dynamics/tools/timingModule.F90
tkealgebraic.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/tkealgebraic.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/cppdefs.h                                                        \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/version.h turbulence.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/tkealgebraic.F90
tkeeq.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/tkeeq.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/cppdefs.h                                                                      \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/version.h turbulence.o util.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/tkeeq.F90
topo_drag.o: $(SRCROOT)atmos_param/topo_drag/topo_drag.F90 fms.o fms_io.o constants.o horiz_interp.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/topo_drag/topo_drag.F90
topography.o: $(SRCROOT)shared/topography/topography.F90 gaussian_topog.o horiz_interp.o fms.o fms_io.o constants.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)shared/topography/topography.F90
tp_core.o: $(SRCROOT)atmos_fv_dynamics/model/tp_core.F90 shr_kind_mod.o fill_module.o mpp.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_fv_dynamics/model/tp_core.F90
tracer_2d.o: $(SRCROOT)atmos_fv_dynamics/model/tracer_2d.F90 fv_pack.o tp_core.o diag_manager.o fv_diagnostics.o shr_kind_mod.o fill_module.o mod_comm.o fv_arrays.o mpp.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_fv_dynamics/model/tracer_2d.F90
tracer_manager.o: $(SRCROOT)shared/tracer_manager/tracer_manager.F90 mpp.o mpp_io.o fms.o field_manager.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)shared/tracer_manager/tracer_manager.F90
transport_matrix.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/transport_matrix.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/include/fms_platform.h field_manager.o mpp.o diag_manager.o ocean_tpm_util.o ocean_types.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/shared/include	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/transport_matrix.F90
tridiagonal.o: $(SRCROOT)shared/tridiagonal/tridiagonal.F90
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)shared/tridiagonal/tridiagonal.F90
tridiagonal_gotm.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/tridiagonal_gotm.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/cppdefs.h                                                      \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/version.h
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/tridiagonal_gotm.F90
tropchem_driver.o: $(SRCROOT)atmos_shared/tracer_driver/tropchem/tropchem_driver.F90 fms.o time_manager.o diag_manager.o tracer_manager.o field_manager.o atmos_tracer_utilities.o constants.o mpp.o interpolator.o time_interp.o mo_chemdr.o mo_chemini.o     \
m_tracname.o moz.mods.o mo_hook.o strat_chem_utilities.o mo_chem_utls.o atmos_sulfate.o esfsw_parameters.o astronomy.o horiz_interp.o fms_io.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_shared/tracer_driver/tropchem/tropchem_driver.F90
turbulence.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/turbulence.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/cppdefs.h                                                            \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/version.h
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/turbulence.F90
update_fv_phys.o: $(SRCROOT)atmos_fv_dynamics/model/update_fv_phys.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/atmos_fv_dynamics/model/fv_arrays.h /home/wenchang/scratch/tiger3/MOM4.1/src/atmos_fv_dynamics/model/fv_point.inc fv_pack.o pft_module.o       \
constants.o field_manager.o tracer_manager.o atmos_nudge.o time_manager.o mod_comm.o mpp.o fv_arrays.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/atmos_fv_dynamics/model	$(SRCROOT)atmos_fv_dynamics/model/update_fv_phys.F90
upper.o: $(SRCROOT)atmos_fv_dynamics/tools/upper.F90
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_fv_dynamics/tools/upper.F90
util.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/util.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/cppdefs.h                                                                              \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/version.h
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/util.F90
uw_clouds_W.o: $(SRCROOT)atmos_param/sea_esf_rad/uw_clouds_W.F90 time_manager.o fms.o constants.o rad_utilities.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/sea_esf_rad/uw_clouds_W.F90
uw_conv.o: $(SRCROOT)atmos_param/shallow_cu/uw_conv.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/include/fms_platform.h mpp.o constants.o diag_manager.o time_manager.o fms.o field_manager.o tracer_manager.o sat_vapor_pres.o                         \
atmos_tracer_utilities.o rad_utilities.o aer_ccn_act.o conv_utilities.o conv_utilities_k.o conv_plumes_k.o conv_closures.o deep_conv.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/shared/include	$(SRCROOT)atmos_param/shallow_cu/uw_conv.F90
variances.o: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/variances.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/cppdefs.h                                                              \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/version.h turbulence.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c -I/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include	/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/variances.F90
vegetation.o: $(SRCROOT)land_lad/vegetation/vegetation.F90 time_manager.o mpp_domains.o land_types.o soil.o constants.o fms.o fms_io.o sat_vapor_pres.o field_manager.o tracer_manager.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)land_lad/vegetation/vegetation.F90
vert_advection.o: $(SRCROOT)atmos_shared/vert_advection/vert_advection.F90 fms.o mpp.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_shared/vert_advection/vert_advection.F90
vert_diff.o: $(SRCROOT)atmos_param/vert_diff/vert_diff.F90 constants.o fms.o field_manager.o tracer_manager.o mpp.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/vert_diff/vert_diff.F90
vert_diff_driver.o: $(SRCROOT)atmos_param/vert_diff_driver/vert_diff_driver.F90 vert_diff.o diag_manager.o time_manager.o fms.o constants.o field_manager.o tracer_manager.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/vert_diff_driver/vert_diff_driver.F90
vert_turb_driver.o: $(SRCROOT)atmos_param/vert_turb_driver/vert_turb_driver.F90 my25_turb.o diffusivity.o edt.o strat_cloud.o shallow_conv.o stable_bl_turb.o entrain.o diag_manager.o time_manager.o constants.o fms.o field_manager.o tracer_manager.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/vert_turb_driver/vert_turb_driver.F90
wet_deposition_0D.o: $(SRCROOT)atmos_param/donner_deep/wet_deposition_0D.F90
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/donner_deep/wet_deposition_0D.F90
write_ocean_data.o: $(SRCROOT)shared/oda_tools/write_ocean_data.F90 mpp_io.o mpp.o oda_types.o time_manager.o mpp_domains.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)shared/oda_tools/write_ocean_data.F90
xbt_drop_rate_adjust.o: $(SRCROOT)shared/oda_tools/xbt_drop_rate_adjust.f90 oda_types.o
	$(FC) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)shared/oda_tools/xbt_drop_rate_adjust.f90
xgrid.o: $(SRCROOT)shared/exchange/xgrid.F90 fms.o mpp.o mpp_domains.o mpp_io.o constants.o mosaic.o stock_constants.o gradient.o time_manager.o diag_manager.o fms_io.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)shared/exchange/xgrid.F90
zeff.o: $(SRCROOT)atmos_param/cosp/quickbeam/zeff.f90 math_lib.o optics_lib.o
	$(FC) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/cosp/quickbeam/zeff.f90
zetac_clouds_W.o: $(SRCROOT)atmos_param/sea_esf_rad/zetac_clouds_W.F90 fms.o constants.o rad_utilities.o microphys_cloud.o
	$(FC) $(CPPDEFS) $(CPPFLAGS) $(FFLAGS) $(OTHERFLAGS) -c	$(SRCROOT)atmos_param/sea_esf_rad/zetac_clouds_W.F90
./mpp_write.h: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_write.h
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_write.h .
./mpp_error_a_a.h: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_error_a_a.h
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_error_a_a.h .
./amip_interp.F90: $(SRCROOT)shared/amip_interp/amip_interp.F90
	cp $(SRCROOT)shared/amip_interp/amip_interp.F90 .
./xbt_drop_rate_adjust.f90: $(SRCROOT)shared/oda_tools/xbt_drop_rate_adjust.f90
	cp $(SRCROOT)shared/oda_tools/xbt_drop_rate_adjust.f90 .
./ocean_velocity_advect.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_velocity_advect.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_velocity_advect.F90 .
./icarus.f: $(SRCROOT)atmos_param/cosp/icarus-scops-3.7/icarus.f
	cp $(SRCROOT)atmos_param/cosp/icarus-scops-3.7/icarus.f .
./diag_manager.F90: $(SRCROOT)shared/diag_manager/diag_manager.F90
	cp $(SRCROOT)shared/diag_manager/diag_manager.F90 .
./platform.F90: $(SRCROOT)shared/platform/platform.F90
	cp $(SRCROOT)shared/platform/platform.F90 .
./atmos_radon.F90: $(SRCROOT)atmos_shared/tracer_driver/atmos_radon.F90
	cp $(SRCROOT)atmos_shared/tracer_driver/atmos_radon.F90 .
./genericeq.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/genericeq.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/genericeq.F90 .
./fms_donner.F90: $(SRCROOT)atmos_param/donner_deep/fms_donner.F90
	cp $(SRCROOT)atmos_param/donner_deep/fms_donner.F90 .
./lagrange.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/lagrange.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/lagrange.F90 .
./specified_clouds_W.F90: $(SRCROOT)atmos_param/sea_esf_rad/specified_clouds_W.F90
	cp $(SRCROOT)atmos_param/sea_esf_rad/specified_clouds_W.F90 .
./ocean_advection_velocity.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_advection_velocity.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_advection_velocity.F90 .
./mpp_io_misc.inc: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_io_misc.inc
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_io_misc.inc .
./mo_photo.F90: $(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_photo.F90
	cp $(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_photo.F90 .
./ocean_sigma_transport.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_sigma_transport.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_sigma_transport.F90 .
./mpp_comm.inc: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_comm.inc
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_comm.inc .
./timingModule.F90: $(SRCROOT)atmos_fv_dynamics/tools/timingModule.F90
	cp $(SRCROOT)atmos_fv_dynamics/tools/timingModule.F90 .
./ocmip2_abiotic.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_bgc/ocmip2_abiotic.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_bgc/ocmip2_abiotic.F90 .
./mpp_global_reduce.h: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_global_reduce.h
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_global_reduce.h .
./ocean_model.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_model.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_model.F90 .
./atmos_sulfur_hex.F90: $(SRCROOT)atmos_shared/tracer_driver/atmos_sulfur_hex.F90
	cp $(SRCROOT)atmos_shared/tracer_driver/atmos_sulfur_hex.F90 .
./conv_utilities.F90: $(SRCROOT)atmos_param/shallow_cu/conv_utilities.F90
	cp $(SRCROOT)atmos_param/shallow_cu/conv_utilities.F90 .
./mo_imp_slv.F90: $(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_imp_slv.F90
	cp $(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_imp_slv.F90 .
./strat_cloud.F90: $(SRCROOT)atmos_param/strat_cloud/strat_cloud.F90
	cp $(SRCROOT)atmos_param/strat_cloud/strat_cloud.F90 .
./strat_clouds_W.F90: $(SRCROOT)atmos_param/sea_esf_rad/strat_clouds_W.F90
	cp $(SRCROOT)atmos_param/sea_esf_rad/strat_clouds_W.F90 .
./ocean_workspace.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_workspace.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_workspace.F90 .
./epsbalgebraic.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/epsbalgebraic.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/epsbalgebraic.F90 .
./ocean_xlandmix.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_xlandmix.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_xlandmix.F90 .
./MersenneTwister.F90: $(SRCROOT)shared/random_numbers/MersenneTwister.F90
	cp $(SRCROOT)shared/random_numbers/MersenneTwister.F90 .
./mpp_chksum.h: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_chksum.h
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_chksum.h .
./ocean_lap_tracer.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_lap_tracer.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_lap_tracer.F90 .
./interp.c: $(SRCROOT)shared/mosaic/interp.c
	cp $(SRCROOT)shared/mosaic/interp.c .
./cloud_obs.F90: $(SRCROOT)atmos_param/cloud_obs/cloud_obs.F90
	cp $(SRCROOT)atmos_param/cloud_obs/cloud_obs.F90 .
./tridiagonal.F90: $(SRCROOT)shared/tridiagonal/tridiagonal.F90
	cp $(SRCROOT)shared/tridiagonal/tridiagonal.F90 .
./system_clock.h: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/system_clock.h
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/system_clock.h .
./mo_chemdr.F90: $(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_chemdr.F90
	cp $(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_chemdr.F90 .
./mo_chemini.F90: $(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_chemini.F90
	cp $(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_chemini.F90 .
./longwave_fluxes.F90: $(SRCROOT)atmos_param/sea_esf_rad/longwave_fluxes.F90
	cp $(SRCROOT)atmos_param/sea_esf_rad/longwave_fluxes.F90 .
./uw_clouds_W.F90: $(SRCROOT)atmos_param/sea_esf_rad/uw_clouds_W.F90
	cp $(SRCROOT)atmos_param/sea_esf_rad/uw_clouds_W.F90 .
./atmos_ch3i.F90: $(SRCROOT)atmos_shared/tracer_driver/atmos_ch3i.F90
	cp $(SRCROOT)atmos_shared/tracer_driver/atmos_ch3i.F90 .
./turbulence.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/turbulence.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/turbulence.F90 .
./ocean_bihcst_friction.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_bihcst_friction.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_bihcst_friction.F90 .
./monin_obukhov_interfaces.h: /home/wenchang/scratch/tiger3/MOM4.1/src/atmos_param/monin_obukhov/monin_obukhov_interfaces.h
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/atmos_param/monin_obukhov/monin_obukhov_interfaces.h .
./write_ocean_data.F90: $(SRCROOT)shared/oda_tools/write_ocean_data.F90
	cp $(SRCROOT)shared/oda_tools/write_ocean_data.F90 .
./dsd.f90: $(SRCROOT)atmos_param/cosp/quickbeam/dsd.f90
	cp $(SRCROOT)atmos_param/cosp/quickbeam/dsd.f90 .
./diff_face.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/diff_face.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/diff_face.F90 .
./flux_exchange.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/coupler/flux_exchange.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/coupler/flux_exchange.F90 .
./ocean_sponges_velocity.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_sponges_velocity.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_sponges_velocity.F90 .
./dissipationeq.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/dissipationeq.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/dissipationeq.F90 .
./donner_deep.F90: $(SRCROOT)atmos_param/donner_deep/donner_deep.F90
	cp $(SRCROOT)atmos_param/donner_deep/donner_deep.F90 .
./standalone_clouds.F90: $(SRCROOT)atmos_param/sea_esf_rad/standalone_clouds.F90
	cp $(SRCROOT)atmos_param/sea_esf_rad/standalone_clouds.F90 .
./atmos_soa.F90: $(SRCROOT)atmos_shared/tracer_driver/atmos_soa.F90
	cp $(SRCROOT)atmos_shared/tracer_driver/atmos_soa.F90 .
./diag_axis.F90: $(SRCROOT)shared/diag_manager/diag_axis.F90
	cp $(SRCROOT)shared/diag_manager/diag_axis.F90 .
./sat_vapor_pres.F90: $(SRCROOT)shared/sat_vapor_pres/sat_vapor_pres.F90
	cp $(SRCROOT)shared/sat_vapor_pres/sat_vapor_pres.F90 .
./gases.f90: $(SRCROOT)atmos_param/cosp/quickbeam/gases.f90
	cp $(SRCROOT)atmos_param/cosp/quickbeam/gases.f90 .
./parse.inc: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/field_manager/parse.inc
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/field_manager/parse.inc .
./horiz_interp_bicubic.F90: $(SRCROOT)shared/horiz_interp/horiz_interp_bicubic.F90
	cp $(SRCROOT)shared/horiz_interp/horiz_interp_bicubic.F90 .
./compute_rist.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/compute_rist.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/compute_rist.F90 .
./init_dry_atm.F90: $(SRCROOT)atmos_fv_dynamics/tools/init_dry_atm.F90
	cp $(SRCROOT)atmos_fv_dynamics/tools/init_dry_atm.F90 .
./format_input.f90: $(SRCROOT)atmos_param/cosp/quickbeam/format_input.f90
	cp $(SRCROOT)atmos_param/cosp/quickbeam/format_input.f90 .
./land_model.F90: $(SRCROOT)land_lad/land_model.F90
	cp $(SRCROOT)land_lad/land_model.F90 .
./memutils.F90: $(SRCROOT)shared/memutils/memutils.F90
	cp $(SRCROOT)shared/memutils/memutils.F90 .
./ocean_shortwave_jerlov.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_shortwave_jerlov.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_shortwave_jerlov.F90 .
./ocean_momentum_source.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_momentum_source.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_momentum_source.F90 .
./mpp_error_a_s.h: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_error_a_s.h
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_error_a_s.h .
./drifters_push.h: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/drifters/drifters_push.h
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/drifters/drifters_push.h .
./read_data_2d.inc: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/fms/read_data_2d.inc
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/fms/read_data_2d.inc .
./sw_core.F90: $(SRCROOT)atmos_fv_dynamics/model/sw_core.F90
	cp $(SRCROOT)atmos_fv_dynamics/model/sw_core.F90 .
./mpp_domains_util.inc: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_domains_util.inc
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_domains_util.inc .
./longwave_params.F90: $(SRCROOT)atmos_param/sea_esf_rad/longwave_params.F90
	cp $(SRCROOT)atmos_param/sea_esf_rad/longwave_params.F90 .
./ocean_lapgen_friction.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_lapgen_friction.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_lapgen_friction.F90 .
./aerosolrad_package.F90: $(SRCROOT)atmos_param/sea_esf_rad/aerosolrad_package.F90
	cp $(SRCROOT)atmos_param/sea_esf_rad/aerosolrad_package.F90 .
./deep_conv.F90: $(SRCROOT)atmos_param/shallow_cu/deep_conv.F90
	cp $(SRCROOT)atmos_param/shallow_cu/deep_conv.F90 .
./init_sw_ic.F90: $(SRCROOT)atmos_fv_dynamics/tools/init_sw_ic.F90
	cp $(SRCROOT)atmos_fv_dynamics/tools/init_sw_ic.F90 .
./soil.F90: $(SRCROOT)land_lad/soil/soil.F90
	cp $(SRCROOT)land_lad/soil/soil.F90 .
./fms.F90: $(SRCROOT)shared/fms/fms.F90
	cp $(SRCROOT)shared/fms/fms.F90 .
./ice_dyn.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/ice_sis/ice_dyn.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/ice_sis/ice_dyn.F90 .
./create_xgrid.h: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mosaic/create_xgrid.h
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mosaic/create_xgrid.h .
./mo_read_sim_chm.F90: $(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_read_sim_chm.F90
	cp $(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_read_sim_chm.F90 .
./ocean_vert_gotm.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_vert_gotm.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_vert_gotm.F90 .
./donner_types.F90: $(SRCROOT)atmos_param/donner_deep/donner_types.F90
	cp $(SRCROOT)atmos_param/donner_deep/donner_types.F90 .
./mpp_io.F90: $(SRCROOT)shared/mpp/mpp_io.F90
	cp $(SRCROOT)shared/mpp/mpp_io.F90 .
./ocean_nphysicsC.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_nphysicsC.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_nphysicsC.F90 .
./donner_meso_k.F90: $(SRCROOT)atmos_param/donner_deep/donner_meso_k.F90
	cp $(SRCROOT)atmos_param/donner_deep/donner_meso_k.F90 .
./drifters_compute_k.h: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/drifters/drifters_compute_k.h
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/drifters/drifters_compute_k.h .
./atmos_sea_salt.F90: $(SRCROOT)atmos_shared/tracer_driver/atmos_sea_salt.F90
	cp $(SRCROOT)atmos_shared/tracer_driver/atmos_sea_salt.F90 .
./co2int.F90: $(SRCROOT)atmos_param/fsrad/co2int.F90
	cp $(SRCROOT)atmos_param/fsrad/co2int.F90 .
./mpp_error_s_a.h: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_error_s_a.h
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_error_s_a.h .
./mpp_chksum_scalar.h: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_chksum_scalar.h
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_chksum_scalar.h .
./read_mosaic.c: $(SRCROOT)shared/mosaic/read_mosaic.c
	cp $(SRCROOT)shared/mosaic/read_mosaic.c .
./tropchem_driver.F90: $(SRCROOT)atmos_shared/tracer_driver/tropchem/tropchem_driver.F90
	cp $(SRCROOT)atmos_shared/tracer_driver/tropchem/tropchem_driver.F90 .
./atmos_ocean_fluxes.F90: $(SRCROOT)shared/coupler/atmos_ocean_fluxes.F90
	cp $(SRCROOT)shared/coupler/atmos_ocean_fluxes.F90 .
./bulkphys_rad.F90: $(SRCROOT)atmos_param/sea_esf_rad/bulkphys_rad.F90
	cp $(SRCROOT)atmos_param/sea_esf_rad/bulkphys_rad.F90 .
./ocean_pressure.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_pressure.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_pressure.F90 .
./bm_omp.F90: $(SRCROOT)atmos_param/betts_miller/bm_omp.F90
	cp $(SRCROOT)atmos_param/betts_miller/bm_omp.F90 .
./ocean_drifters.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_diag/ocean_drifters.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_diag/ocean_drifters.F90 .
./mrgrnk.f90: $(SRCROOT)atmos_param/cosp/quickbeam/mrgrnk.f90
	cp $(SRCROOT)atmos_param/cosp/quickbeam/mrgrnk.f90 .
./esfsw_driver.F90: $(SRCROOT)atmos_param/sea_esf_rad/esfsw_driver.F90
	cp $(SRCROOT)atmos_param/sea_esf_rad/esfsw_driver.F90 .
./ocean_diagnostics.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_diag/ocean_diagnostics.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_diag/ocean_diagnostics.F90 .
./zeff.f90: $(SRCROOT)atmos_param/cosp/quickbeam/zeff.f90
	cp $(SRCROOT)atmos_param/cosp/quickbeam/zeff.f90 .
./aer_ccn_act_k.F90: $(SRCROOT)atmos_shared/tracer_driver/aer_ccn_act/aer_ccn_act_k.F90
	cp $(SRCROOT)atmos_shared/tracer_driver/aer_ccn_act/aer_ccn_act_k.F90 .
./mpp_io_connect.inc: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_io_connect.inc
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_io_connect.inc .
./hconst.F90: $(SRCROOT)atmos_param/fsrad/hconst.F90
	cp $(SRCROOT)atmos_param/fsrad/hconst.F90 .
./mpp_transmit_mpi.h: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_transmit_mpi.h
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_transmit_mpi.h .
./clouds.F90: $(SRCROOT)atmos_param/clouds/clouds.F90
	cp $(SRCROOT)atmos_param/clouds/clouds.F90 .
./cloud_spec.F90: $(SRCROOT)atmos_param/sea_esf_rad/cloud_spec.F90
	cp $(SRCROOT)atmos_param/sea_esf_rad/cloud_spec.F90 .
./ode_solvers.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/ode_solvers.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/ode_solvers.F90 .
./interpolator.F90: $(SRCROOT)atmos_shared/interpolator/interpolator.F90
	cp $(SRCROOT)atmos_shared/interpolator/interpolator.F90 .
./monin_obukhov.F90: $(SRCROOT)atmos_param/monin_obukhov/monin_obukhov.F90
	cp $(SRCROOT)atmos_param/monin_obukhov/monin_obukhov.F90 .
./read_mosaic.h: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mosaic/read_mosaic.h
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mosaic/read_mosaic.h .
./shortwave_driver.F90: $(SRCROOT)atmos_param/sea_esf_rad/shortwave_driver.F90
	cp $(SRCROOT)atmos_param/sea_esf_rad/shortwave_driver.F90 .
./ocean_shortwave_gfdl.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_shortwave_gfdl.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_shortwave_gfdl.F90 .
./kbeq.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/kbeq.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/kbeq.F90 .
./load_mie_table.f90: $(SRCROOT)atmos_param/cosp/quickbeam/load_mie_table.f90
	cp $(SRCROOT)atmos_param/cosp/quickbeam/load_mie_table.f90 .
./diffusivity.F90: $(SRCROOT)atmos_param/diffusivity/diffusivity.F90
	cp $(SRCROOT)atmos_param/diffusivity/diffusivity.F90 .
./ocean_passive.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_passive.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_passive.F90 .
./mpp_pset.F90: $(SRCROOT)shared/mpp/mpp_pset.F90
	cp $(SRCROOT)shared/mpp/mpp_pset.F90 .
./mpp.F90: $(SRCROOT)shared/mpp/mpp.F90
	cp $(SRCROOT)shared/mpp/mpp.F90 .
./mpp_global_sum.h: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_global_sum.h
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_global_sum.h .
./microphys_rad.F90: $(SRCROOT)atmos_param/sea_esf_rad/microphys_rad.F90
	cp $(SRCROOT)atmos_param/sea_esf_rad/microphys_rad.F90 .
./longwave.F90: $(SRCROOT)atmos_param/fsrad/longwave.F90
	cp $(SRCROOT)atmos_param/fsrad/longwave.F90 .
./mpp_sum_sma.h: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_sum_sma.h
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_sum_sma.h .
./land_properties.F90: $(SRCROOT)land_lad/soil/land_properties.F90
	cp $(SRCROOT)land_lad/soil/land_properties.F90 .
./edt.F90: $(SRCROOT)atmos_param/edt/edt.F90
	cp $(SRCROOT)atmos_param/edt/edt.F90 .
./age_of_air.F90: $(SRCROOT)atmos_fv_dynamics/tools/age_of_air.F90
	cp $(SRCROOT)atmos_fv_dynamics/tools/age_of_air.F90 .
./variances.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/variances.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/variances.F90 .
./fms_switches.h: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/drifters/fms_switches.h
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/drifters/fms_switches.h .
./betaDistribution.F90: $(SRCROOT)atmos_param/cloud_generator/betaDistribution.F90
	cp $(SRCROOT)atmos_param/cloud_generator/betaDistribution.F90 .
./drifters_input.F90: $(SRCROOT)shared/drifters/drifters_input.F90
	cp $(SRCROOT)shared/drifters/drifters_input.F90 .
./interp.h: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mosaic/interp.h
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mosaic/interp.h .
./ocean_nphysics_util.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_nphysics_util.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_nphysics_util.F90 .
./donner_types.h: /home/wenchang/scratch/tiger3/MOM4.1/src/atmos_param/donner_deep/donner_types.h
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/atmos_param/donner_deep/donner_types.h .
./fv_pack.F90: $(SRCROOT)atmos_fv_dynamics/model/fv_pack.F90
	cp $(SRCROOT)atmos_fv_dynamics/model/fv_pack.F90 .
./astronomy.F90: $(SRCROOT)shared/astronomy/astronomy.F90
	cp $(SRCROOT)shared/astronomy/astronomy.F90 .
./ocean_xlandinsert.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_xlandinsert.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_xlandinsert.F90 .
./ocean_coriolis.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_coriolis.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_coriolis.F90 .
./read_data_4d.inc: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/fms/read_data_4d.inc
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/fms/read_data_4d.inc .
./cloudrad_diagnostics.F90: $(SRCROOT)atmos_param/sea_esf_rad/cloudrad_diagnostics.F90
	cp $(SRCROOT)atmos_param/sea_esf_rad/cloudrad_diagnostics.F90 .
./eqstate.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/eqstate.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/eqstate.F90 .
./mpp_global_field.h: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_global_field.h
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_global_field.h .
./mpp_get_boundary.h: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_get_boundary.h
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_get_boundary.h .
./ocmip2_he.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_bgc/ocmip2_he.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_bgc/ocmip2_he.F90 .
./tkeeq.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/tkeeq.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/tkeeq.F90 .
./set_eta.F90: $(SRCROOT)atmos_fv_dynamics/tools/set_eta.F90
	cp $(SRCROOT)atmos_fv_dynamics/tools/set_eta.F90 .
./cmue_c.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/cmue_c.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/cmue_c.F90 .
./ocean_residency.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_residency.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_residency.F90 .
./nsclock.c: $(SRCROOT)shared/mpp/nsclock.c
	cp $(SRCROOT)shared/mpp/nsclock.c .
./mo_hook.F90: $(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_hook.F90
	cp $(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_hook.F90 .
./lidar_simulator.f90: $(SRCROOT)atmos_param/cosp/actsim/lidar_simulator.f90
	cp $(SRCROOT)atmos_param/cosp/actsim/lidar_simulator.f90 .
./ocmip2_co2calc.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_bgc/ocmip2_co2calc.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_bgc/ocmip2_co2calc.F90 .
./mpp_util_sma.inc: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_util_sma.inc
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_util_sma.inc .
./monin_obukhov_kernel.F90: $(SRCROOT)atmos_param/monin_obukhov/monin_obukhov_kernel.F90
	cp $(SRCROOT)atmos_param/monin_obukhov/monin_obukhov_kernel.F90 .
./mo_chem_utls.F90: $(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_chem_utls.F90
	cp $(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_chem_utls.F90 .
./mpp_data_sma.inc: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_data_sma.inc
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_data_sma.inc .
./ocean_vert_const.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_vert_const.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_vert_const.F90 .
./sealw99.F90: $(SRCROOT)atmos_param/sea_esf_rad/sealw99.F90
	cp $(SRCROOT)atmos_param/sea_esf_rad/sealw99.F90 .
./ocean_domains.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_domains.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_domains.F90 .
./donner_deep_miz.F90: $(SRCROOT)atmos_param/donner_deep/donner_deep_miz.F90
	cp $(SRCROOT)atmos_param/donner_deep/donner_deep_miz.F90 .
./atmos_age_tracer.F90: $(SRCROOT)atmos_shared/tracer_driver/atmos_age_tracer.F90
	cp $(SRCROOT)atmos_shared/tracer_driver/atmos_age_tracer.F90 .
./diag_data.F90: $(SRCROOT)shared/diag_manager/diag_data.F90
	cp $(SRCROOT)shared/diag_manager/diag_data.F90 .
./horiz_interp_conserve.F90: $(SRCROOT)shared/horiz_interp/horiz_interp_conserve.F90
	cp $(SRCROOT)shared/horiz_interp/horiz_interp_conserve.F90 .
./ocean_topog.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_topog.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_topog.F90 .
./diag_cloud.F90: $(SRCROOT)atmos_param/diag_cloud/diag_cloud.F90
	cp $(SRCROOT)atmos_param/diag_cloud/diag_cloud.F90 .
./fv_dynamics.F90: $(SRCROOT)atmos_fv_dynamics/model/fv_dynamics.F90
	cp $(SRCROOT)atmos_fv_dynamics/model/fv_dynamics.F90 .
./mg_drag.F90: $(SRCROOT)atmos_param/mg_drag/mg_drag.F90
	cp $(SRCROOT)atmos_param/mg_drag/mg_drag.F90 .
./strat_chem_driver.F90: $(SRCROOT)atmos_shared/tracer_driver/stratchem/strat_chem_driver.F90
	cp $(SRCROOT)atmos_shared/tracer_driver/stratchem/strat_chem_driver.F90 .
./rot.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/ice_sis/rot.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/ice_sis/rot.F90 .
./ocean_mixdownslope.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_mixdownslope.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_mixdownslope.F90 .
./fms_io.F90: $(SRCROOT)shared/fms/fms_io.F90
	cp $(SRCROOT)shared/fms/fms_io.F90 .
./mpp_reduce_nocomm.h: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_reduce_nocomm.h
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_reduce_nocomm.h .
./get_cal_time.F90: $(SRCROOT)shared/time_manager/get_cal_time.F90
	cp $(SRCROOT)shared/time_manager/get_cal_time.F90 .
./ocean_vert_kpp_mom4p0.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_vert_kpp_mom4p0.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_vert_kpp_mom4p0.F90 .
./algebraiclength.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/algebraiclength.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/algebraiclength.F90 .
./axis_utils.F90: $(SRCROOT)shared/axis_utils/axis_utils.F90
	cp $(SRCROOT)shared/axis_utils/axis_utils.F90 .
./ocean_form_drag.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_form_drag.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_form_drag.F90 .
./cosp.f90: $(SRCROOT)atmos_param/cosp/cosp.f90
	cp $(SRCROOT)atmos_param/cosp/cosp.f90 .
./data_override.F90: $(SRCROOT)shared/data_override/data_override.F90
	cp $(SRCROOT)shared/data_override/data_override.F90 .
./ocean_tpm_util.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_tpm_util.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_tpm_util.F90 .
./q2over2eq.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/q2over2eq.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/q2over2eq.F90 .
./cosp_constants.f90: $(SRCROOT)atmos_param/cosp/cosp_constants.f90
	cp $(SRCROOT)atmos_param/cosp/cosp_constants.f90 .
./ocean_sbc.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_sbc.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_sbc.F90 .
./cloud_interpolator.F90: $(SRCROOT)shared/drifters/cloud_interpolator.F90
	cp $(SRCROOT)shared/drifters/cloud_interpolator.F90 .
./cmue_rf.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/cmue_rf.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/cmue_rf.F90 .
./atmos_tracer_driver.F90: $(SRCROOT)atmos_shared/tracer_driver/atmos_tracer_driver.F90
	cp $(SRCROOT)atmos_shared/tracer_driver/atmos_tracer_driver.F90 .
./ice_model.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/ice_sis/ice_model.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/ice_sis/ice_model.F90 .
./donner_utilities_k.F90: $(SRCROOT)atmos_param/donner_deep/donner_utilities_k.F90
	cp $(SRCROOT)atmos_param/donner_deep/donner_utilities_k.F90 .
./mod_comm.F90: $(SRCROOT)atmos_fv_dynamics/tools/mod_comm.F90
	cp $(SRCROOT)atmos_fv_dynamics/tools/mod_comm.F90 .
./llnl_stats.f90: $(SRCROOT)atmos_param/cosp/llnl/llnl_stats.f90
	cp $(SRCROOT)atmos_param/cosp/llnl/llnl_stats.f90 .
./cppdefs.h: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/cppdefs.h
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/cppdefs.h .
./ocean_overflow.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_overflow.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_overflow.F90 .
./wet_deposition_0D.F90: $(SRCROOT)atmos_param/donner_deep/wet_deposition_0D.F90
	cp $(SRCROOT)atmos_param/donner_deep/wet_deposition_0D.F90 .
./radiation_diag.F90: $(SRCROOT)atmos_param/sea_esf_rad/radiation_diag.F90
	cp $(SRCROOT)atmos_param/sea_esf_rad/radiation_diag.F90 .
./atmos_convection_tracer.F90: $(SRCROOT)atmos_shared/tracer_driver/atmos_convection_tracer.F90
	cp $(SRCROOT)atmos_shared/tracer_driver/atmos_convection_tracer.F90 .
./cloud_rad.F90: $(SRCROOT)atmos_param/cloud_rad/cloud_rad.F90
	cp $(SRCROOT)atmos_param/cloud_rad/cloud_rad.F90 .
./cosp_simulator.f90: $(SRCROOT)atmos_param/cosp/cosp_simulator.f90
	cp $(SRCROOT)atmos_param/cosp/cosp_simulator.f90 .
./coupler_main.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/coupler/coupler_main.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/coupler/coupler_main.F90 .
./sea_esf_rad.F90: $(SRCROOT)atmos_param/sea_esf_rad/sea_esf_rad.F90
	cp $(SRCROOT)atmos_param/sea_esf_rad/sea_esf_rad.F90 .
./mpp_transmit_nocomm.h: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_transmit_nocomm.h
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_transmit_nocomm.h .
./ocean_shortwave_csiro.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_shortwave_csiro.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_shortwave_csiro.F90 .
./mosaic.F90: $(SRCROOT)shared/mosaic/mosaic.F90
	cp $(SRCROOT)shared/mosaic/mosaic.F90 .
./ocean_vert_mix.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_vert_mix.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_vert_mix.F90 .
./drifters_comm.F90: $(SRCROOT)shared/drifters/drifters_comm.F90
	cp $(SRCROOT)shared/drifters/drifters_comm.F90 .
./mpp_chksum_int.h: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_chksum_int.h
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_chksum_int.h .
./ocean_polar_filter.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_polar_filter.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_polar_filter.F90 .
./donner_lite_k.F90: $(SRCROOT)atmos_param/donner_deep/donner_lite_k.F90
	cp $(SRCROOT)atmos_param/donner_deep/donner_lite_k.F90 .
./version.h: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/version.h
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/version.h .
./climap_albedo.F90: $(SRCROOT)land_param/climap_albedo.F90
	cp $(SRCROOT)land_param/climap_albedo.F90 .
./diag_clouds_W.F90: $(SRCROOT)atmos_param/sea_esf_rad/diag_clouds_W.F90
	cp $(SRCROOT)atmos_param/sea_esf_rad/diag_clouds_W.F90 .
./mcm_swnew.F90: $(SRCROOT)atmos_param/fsrad/mcm_swnew.F90
	cp $(SRCROOT)atmos_param/fsrad/mcm_swnew.F90 .
./time_interp.F90: $(SRCROOT)shared/time_interp/time_interp.F90
	cp $(SRCROOT)shared/time_interp/time_interp.F90 .
./kbalgebraic.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/kbalgebraic.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/kbalgebraic.F90 .
./pft_module.F90: $(SRCROOT)atmos_fv_dynamics/model/pft_module.F90
	cp $(SRCROOT)atmos_fv_dynamics/model/pft_module.F90 .
./ocean_vert_pp.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_vert_pp.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_vert_pp.F90 .
./cosp_driver.F90: $(SRCROOT)atmos_param/cosp/cosp_driver.F90
	cp $(SRCROOT)atmos_param/cosp/cosp_driver.F90 .
./cosp_types.f90: $(SRCROOT)atmos_param/cosp/cosp_types.f90
	cp $(SRCROOT)atmos_param/cosp/cosp_types.f90 .
./ocean_tracer_advect.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_tracer_advect.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_tracer_advect.F90 .
./moz.mat.F90: $(SRCROOT)atmos_shared/tracer_driver/tropchem/moz.mat.F90
	cp $(SRCROOT)atmos_shared/tracer_driver/tropchem/moz.mat.F90 .
./rivers.F90: $(SRCROOT)land_lad/soil/rivers.F90
	cp $(SRCROOT)land_lad/soil/rivers.F90 .
./moist_processes_utils.F90: $(SRCROOT)atmos_param/moist_processes/moist_processes_utils.F90
	cp $(SRCROOT)atmos_param/moist_processes/moist_processes_utils.F90 .
./mpp_do_check.h: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_do_check.h
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_do_check.h .
./ocean_tracer_diag.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_diag/ocean_tracer_diag.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_diag/ocean_tracer_diag.F90 .
./mpp_comm_mpi.inc: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_comm_mpi.inc
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_comm_mpi.inc .
./ocean_thickness.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_thickness.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_thickness.F90 .
./donner_deep_clouds_W.F90: $(SRCROOT)atmos_param/sea_esf_rad/donner_deep_clouds_W.F90
	cp $(SRCROOT)atmos_param/sea_esf_rad/donner_deep_clouds_W.F90 .
./transport_matrix.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/transport_matrix.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/transport_matrix.F90 .
./atmos_co2.F90: $(SRCROOT)atmos_shared/tracer_driver/atmos_co2.F90
	cp $(SRCROOT)atmos_shared/tracer_driver/atmos_co2.F90 .
./oda_types.F90: $(SRCROOT)shared/oda_tools/oda_types.F90
	cp $(SRCROOT)shared/oda_tools/oda_types.F90 .
./moist_processes.F90: $(SRCROOT)atmos_param/moist_processes/moist_processes.F90
	cp $(SRCROOT)atmos_param/moist_processes/moist_processes.F90 .
./FMS_coupler_util.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/ocean_shared/generic_tracers/FMS_coupler_util.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/ocean_shared/generic_tracers/FMS_coupler_util.F90 .
./mcm_lw.F90: $(SRCROOT)atmos_param/fsrad/mcm_lw.F90
	cp $(SRCROOT)atmos_param/fsrad/mcm_lw.F90 .
./getmax.F90: $(SRCROOT)atmos_fv_dynamics/tools/getmax.F90
	cp $(SRCROOT)atmos_fv_dynamics/tools/getmax.F90 .
./update_fv_phys.F90: $(SRCROOT)atmos_fv_dynamics/model/update_fv_phys.F90
	cp $(SRCROOT)atmos_fv_dynamics/model/update_fv_phys.F90 .
./donner_deep_k.F90: $(SRCROOT)atmos_param/donner_deep/donner_deep_k.F90
	cp $(SRCROOT)atmos_param/donner_deep/donner_deep_k.F90 .
./cosp_lidar.f90: $(SRCROOT)atmos_param/cosp/cosp_lidar.f90
	cp $(SRCROOT)atmos_param/cosp/cosp_lidar.f90 .
./ocean_age_tracer.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_age_tracer.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_age_tracer.F90 .
./drifters.F90: $(SRCROOT)shared/drifters/drifters.F90
	cp $(SRCROOT)shared/drifters/drifters.F90 .
./ocean_sponges_eta.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_sponges_eta.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_sponges_eta.F90 .
./scops.f: $(SRCROOT)atmos_param/cosp/icarus-scops-3.7/scops.f
	cp $(SRCROOT)atmos_param/cosp/icarus-scops-3.7/scops.f .
./ocean_residency_ml.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_residency_ml.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_residency_ml.F90 .
./ice_albedo.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/ice_param/ice_albedo.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/ice_param/ice_albedo.F90 .
./cmue_d.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/cmue_d.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/cmue_d.F90 .
./mo_setinv.F90: $(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_setinv.F90
	cp $(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_setinv.F90 .
./alpha_mnb.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/alpha_mnb.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/alpha_mnb.F90 .
./ocean_parameters.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_parameters.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_parameters.F90 .
./longwave_tables.F90: $(SRCROOT)atmos_param/sea_esf_rad/longwave_tables.F90
	cp $(SRCROOT)atmos_param/sea_esf_rad/longwave_tables.F90 .
./ras.F90: $(SRCROOT)atmos_param/ras/ras.F90
	cp $(SRCROOT)atmos_param/ras/ras.F90 .
./ocean_adv_vel_diag.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_diag/ocean_adv_vel_diag.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_diag/ocean_adv_vel_diag.F90 .
./ocean_tempsalt.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_tempsalt.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_tempsalt.F90 .
./gmean.F90: $(SRCROOT)atmos_fv_dynamics/tools/gmean.F90
	cp $(SRCROOT)atmos_fv_dynamics/tools/gmean.F90 .
./kpp.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/kpp.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/kpp.F90 .
./ocean_pert_co2.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_bgc/ocean_pert_co2.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_bgc/ocean_pert_co2.F90 .
./conv_plumes.F90: $(SRCROOT)atmos_param/shallow_cu/conv_plumes.F90
	cp $(SRCROOT)atmos_param/shallow_cu/conv_plumes.F90 .
./ocean_obc.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_obc.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_obc.F90 .
./moz.mods.F90: $(SRCROOT)atmos_shared/tracer_driver/tropchem/moz.mods.F90
	cp $(SRCROOT)atmos_shared/tracer_driver/tropchem/moz.mods.F90 .
./uw_conv.F90: $(SRCROOT)atmos_param/shallow_cu/uw_conv.F90
	cp $(SRCROOT)atmos_param/shallow_cu/uw_conv.F90 .
./physics_driver.F90: $(SRCROOT)atmos_param/physics_driver/physics_driver.F90
	cp $(SRCROOT)atmos_param/physics_driver/physics_driver.F90 .
./grid.F90: $(SRCROOT)shared/mosaic/grid.F90
	cp $(SRCROOT)shared/mosaic/grid.F90 .
./vert_advection.F90: $(SRCROOT)atmos_shared/vert_advection/vert_advection.F90
	cp $(SRCROOT)atmos_shared/vert_advection/vert_advection.F90 .
./cloudrad_package.F90: $(SRCROOT)atmos_param/sea_esf_rad/cloudrad_package.F90
	cp $(SRCROOT)atmos_param/sea_esf_rad/cloudrad_package.F90 .
./betts_miller.F90: $(SRCROOT)atmos_param/betts_miller/betts_miller.F90
	cp $(SRCROOT)atmos_param/betts_miller/betts_miller.F90 .
./rad_diag.F90: $(SRCROOT)atmos_param/fsrad/rad_diag.F90
	cp $(SRCROOT)atmos_param/fsrad/rad_diag.F90 .
./math_lib.f90: $(SRCROOT)atmos_param/cosp/quickbeam/math_lib.f90
	cp $(SRCROOT)atmos_param/cosp/quickbeam/math_lib.f90 .
./tracer_manager.F90: $(SRCROOT)shared/tracer_manager/tracer_manager.F90
	cp $(SRCROOT)shared/tracer_manager/tracer_manager.F90 .
./rad_utilities.F90: $(SRCROOT)atmos_param/sea_esf_rad/rad_utilities.F90
	cp $(SRCROOT)atmos_param/sea_esf_rad/rad_utilities.F90 .
./gradient.F90: $(SRCROOT)shared/mosaic/gradient.F90
	cp $(SRCROOT)shared/mosaic/gradient.F90 .
./ocean_tracer_util.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_diag/ocean_tracer_util.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_diag/ocean_tracer_util.F90 .
./esfsw_parameters.F90: $(SRCROOT)atmos_param/sea_esf_rad/esfsw_parameters.F90
	cp $(SRCROOT)atmos_param/sea_esf_rad/esfsw_parameters.F90 .
./mpp_util_nocomm.inc: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_util_nocomm.inc
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_util_nocomm.inc .
./diff_center.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/diff_center.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/diff_center.F90 .
./atmosphere.F90: $(SRCROOT)atmos_fv_dynamics/driver/coupled/atmosphere.F90
	cp $(SRCROOT)atmos_fv_dynamics/driver/coupled/atmosphere.F90 .
./horiz_interp_spherical.F90: $(SRCROOT)shared/horiz_interp/horiz_interp_spherical.F90
	cp $(SRCROOT)shared/horiz_interp/horiz_interp_spherical.F90 .
./ecmfft.F90: $(SRCROOT)atmos_fv_dynamics/model/ecmfft.F90
	cp $(SRCROOT)atmos_fv_dynamics/model/ecmfft.F90 .
./mpp_do_redistribute.h: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_do_redistribute.h
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_do_redistribute.h .
./dyn_core.F90: $(SRCROOT)atmos_fv_dynamics/model/dyn_core.F90
	cp $(SRCROOT)atmos_fv_dynamics/model/dyn_core.F90 .
./atmos_lib.f90: $(SRCROOT)atmos_param/cosp/quickbeam/atmos_lib.f90
	cp $(SRCROOT)atmos_param/cosp/quickbeam/atmos_lib.f90 .
./ocean_velocity.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_velocity.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_velocity.F90 .
./ocean_bih_tracer.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_bih_tracer.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_bih_tracer.F90 .
./ocean_increment_tracer.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_increment_tracer.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_increment_tracer.F90 .
./ocean_barotropic.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_barotropic.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_barotropic.F90 .
./mpp_global_sum_tl.h: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_global_sum_tl.h
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_global_sum_tl.h .
./fft99.F90: $(SRCROOT)shared/fft/fft99.F90
	cp $(SRCROOT)shared/fft/fft99.F90 .
./conv_closures.F90: $(SRCROOT)atmos_param/shallow_cu/conv_closures.F90
	cp $(SRCROOT)atmos_param/shallow_cu/conv_closures.F90 .
./shr_kind_mod.F90: $(SRCROOT)atmos_fv_dynamics/model/shr_kind_mod.F90
	cp $(SRCROOT)atmos_fv_dynamics/model/shr_kind_mod.F90 .
./mo_setsox.F90: $(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_setsox.F90
	cp $(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_setsox.F90 .
./ocean_memory.h: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_memory.h
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_memory.h .
./fv_point.inc: /home/wenchang/scratch/tiger3/MOM4.1/src/atmos_fv_dynamics/model/fv_point.inc
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/atmos_fv_dynamics/model/fv_point.inc .
./ispralength.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/ispralength.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/ispralength.F90 .
./radar_simulator.f90: $(SRCROOT)atmos_param/cosp/quickbeam/radar_simulator.f90
	cp $(SRCROOT)atmos_param/cosp/quickbeam/radar_simulator.f90 .
./cloud_generator.F90: $(SRCROOT)atmos_param/cloud_generator/cloud_generator.F90
	cp $(SRCROOT)atmos_param/cloud_generator/cloud_generator.F90 .
./fv_arrays.F90: $(SRCROOT)atmos_fv_dynamics/model/fv_arrays.F90
	cp $(SRCROOT)atmos_fv_dynamics/model/fv_arrays.F90 .
./lscale_cond.F90: $(SRCROOT)atmos_param/lscale_cond/lscale_cond.F90
	cp $(SRCROOT)atmos_param/lscale_cond/lscale_cond.F90 .
./fv_physics.F90: $(SRCROOT)atmos_fv_dynamics/driver/coupled/fv_physics.F90
	cp $(SRCROOT)atmos_fv_dynamics/driver/coupled/fv_physics.F90 .
./surface_flux.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/coupler/surface_flux.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/coupler/surface_flux.F90 .
./atmos_carbon_aerosol.F90: $(SRCROOT)atmos_shared/tracer_driver/atmos_carbon_aerosol.F90
	cp $(SRCROOT)atmos_shared/tracer_driver/atmos_carbon_aerosol.F90 .
./ocean_operators.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_operators.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_operators.F90 .
./conv_utilities_k.F90: $(SRCROOT)atmos_param/shallow_cu/conv_utilities_k.F90
	cp $(SRCROOT)atmos_param/shallow_cu/conv_utilities_k.F90 .
./grey_radiation.F90: $(SRCROOT)atmos_param/grey_radiation/grey_radiation.F90
	cp $(SRCROOT)atmos_param/grey_radiation/grey_radiation.F90 .
./donner_rad_k.F90: $(SRCROOT)atmos_param/donner_deep/donner_rad_k.F90
	cp $(SRCROOT)atmos_param/donner_deep/donner_rad_k.F90 .
./lmd_ipsl_stats.f90: $(SRCROOT)atmos_param/cosp/actsim/lmd_ipsl_stats.f90
	cp $(SRCROOT)atmos_param/cosp/actsim/lmd_ipsl_stats.f90 .
./mpp_data.F90: $(SRCROOT)shared/mpp/mpp_data.F90
	cp $(SRCROOT)shared/mpp/mpp_data.F90 .
./load_hydrometeor_classes.f90: $(SRCROOT)atmos_param/cosp/quickbeam/load_hydrometeor_classes.f90
	cp $(SRCROOT)atmos_param/cosp/quickbeam/load_hydrometeor_classes.f90 .
./vert_diff.F90: $(SRCROOT)atmos_param/vert_diff/vert_diff.F90
	cp $(SRCROOT)atmos_param/vert_diff/vert_diff.F90 .
./ocmip2_cfc.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_bgc/ocmip2_cfc.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_bgc/ocmip2_cfc.F90 .
./atmos_nudge.F90: $(SRCROOT)atmos_shared/atmos_nudge/atmos_nudge.F90
	cp $(SRCROOT)atmos_shared/atmos_nudge/atmos_nudge.F90 .
./gridinterpol.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/gridinterpol.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/gridinterpol.F90 .
./diag_output.F90: $(SRCROOT)shared/diag_manager/diag_output.F90
	cp $(SRCROOT)shared/diag_manager/diag_output.F90 .
./mpp_data_nocomm.inc: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_data_nocomm.inc
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_data_nocomm.inc .
./mpp_do_checkV.h: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_do_checkV.h
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_do_checkV.h .
./fill_module.F90: $(SRCROOT)atmos_fv_dynamics/model/fill_module.F90
	cp $(SRCROOT)atmos_fv_dynamics/model/fill_module.F90 .
./ocean_riverspread.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_riverspread.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_riverspread.F90 .
./ocean_velocity_diag.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_diag/ocean_velocity_diag.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_diag/ocean_velocity_diag.F90 .
./constant.h: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mosaic/constant.h
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mosaic/constant.h .
./cosp_isccp_simulator.f90: $(SRCROOT)atmos_param/cosp/cosp_isccp_simulator.f90
	cp $(SRCROOT)atmos_param/cosp/cosp_isccp_simulator.f90 .
./entrain.F90: $(SRCROOT)atmos_param/entrain/entrain.F90
	cp $(SRCROOT)atmos_param/entrain/entrain.F90 .
./rad_output_file.F90: $(SRCROOT)atmos_param/sea_esf_rad/rad_output_file.F90
	cp $(SRCROOT)atmos_param/sea_esf_rad/rad_output_file.F90 .
./fs_profile.F90: $(SRCROOT)atmos_param/fsrad/fs_profile.F90
	cp $(SRCROOT)atmos_param/fsrad/fs_profile.F90 .
./donner_cloud_model_k.F90: $(SRCROOT)atmos_param/donner_deep/donner_cloud_model_k.F90
	cp $(SRCROOT)atmos_param/donner_deep/donner_cloud_model_k.F90 .
./ocean_lap_friction.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_lap_friction.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_lap_friction.F90 .
./fft.F90: $(SRCROOT)shared/fft/fft.F90
	cp $(SRCROOT)shared/fft/fft.F90 .
./cloud_zonal.F90: $(SRCROOT)atmos_param/cloud_zonal/cloud_zonal.F90
	cp $(SRCROOT)atmos_param/cloud_zonal/cloud_zonal.F90 .
./horiz_interp_type.F90: $(SRCROOT)shared/horiz_interp/horiz_interp_type.F90
	cp $(SRCROOT)shared/horiz_interp/horiz_interp_type.F90 .
./mpp_parameter.F90: $(SRCROOT)shared/mpp/mpp_parameter.F90
	cp $(SRCROOT)shared/mpp/mpp_parameter.F90 .
./ocean_lapcst_friction.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_lapcst_friction.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_lapcst_friction.F90 .
./ocean_frazil.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_frazil.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_frazil.F90 .
./aerosol.F90: $(SRCROOT)atmos_param/sea_esf_rad/aerosol.F90
	cp $(SRCROOT)atmos_param/sea_esf_rad/aerosol.F90 .
./ocean_density.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_density.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_density.F90 .
./par_vecsum.F90: $(SRCROOT)atmos_fv_dynamics/tools/par_vecsum.F90
	cp $(SRCROOT)atmos_fv_dynamics/tools/par_vecsum.F90 .
./radiative_gases.F90: $(SRCROOT)atmos_param/sea_esf_rad/radiative_gases.F90
	cp $(SRCROOT)atmos_param/sea_esf_rad/radiative_gases.F90 .
./moz.subs.F90: $(SRCROOT)atmos_shared/tracer_driver/tropchem/moz.subs.F90
	cp $(SRCROOT)atmos_shared/tracer_driver/tropchem/moz.subs.F90 .
./hs_forcing.F90: $(SRCROOT)atmos_param/hs_forcing/hs_forcing.F90
	cp $(SRCROOT)atmos_param/hs_forcing/hs_forcing.F90 .
./generic_tracer.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/ocean_shared/generic_tracers/generic_tracer.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/ocean_shared/generic_tracers/generic_tracer.F90 .
./horiz_interp_bilinear.F90: $(SRCROOT)shared/horiz_interp/horiz_interp_bilinear.F90
	cp $(SRCROOT)shared/horiz_interp/horiz_interp_bilinear.F90 .
./random_numbers.F90: $(SRCROOT)shared/random_numbers/random_numbers.F90
	cp $(SRCROOT)shared/random_numbers/random_numbers.F90 .
./mpp_read_2Ddecomp.h: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_read_2Ddecomp.h
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_read_2Ddecomp.h .
./time_manager.F90: $(SRCROOT)shared/time_manager/time_manager.F90
	cp $(SRCROOT)shared/time_manager/time_manager.F90 .
./coupler_types.F90: $(SRCROOT)shared/coupler/coupler_types.F90
	cp $(SRCROOT)shared/coupler/coupler_types.F90 .
./stock_constants.F90: $(SRCROOT)shared/exchange/stock_constants.F90
	cp $(SRCROOT)shared/exchange/stock_constants.F90 .
./gaussian_topog.F90: $(SRCROOT)shared/topography/gaussian_topog.F90
	cp $(SRCROOT)shared/topography/gaussian_topog.F90 .
./vegetation.F90: $(SRCROOT)land_lad/vegetation/vegetation.F90
	cp $(SRCROOT)land_lad/vegetation/vegetation.F90 .
./fv_diagnostics.F90: $(SRCROOT)atmos_fv_dynamics/tools/fv_diagnostics.F90
	cp $(SRCROOT)atmos_fv_dynamics/tools/fv_diagnostics.F90 .
./mosaic_util.h: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mosaic/mosaic_util.h
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mosaic/mosaic_util.h .
./production.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/production.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/production.F90 .
./cumulus_closure_k.F90: $(SRCROOT)atmos_param/donner_deep/cumulus_closure_k.F90
	cp $(SRCROOT)atmos_param/donner_deep/cumulus_closure_k.F90 .
./adv_center.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/adv_center.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/adv_center.F90 .
./cmue_sg.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/cmue_sg.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/cmue_sg.F90 .
./drifters_core.F90: $(SRCROOT)shared/drifters/drifters_core.F90
	cp $(SRCROOT)shared/drifters/drifters_core.F90 .
./mpp_domains_comm.inc: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_domains_comm.inc
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_domains_comm.inc .
./land_types.F90: $(SRCROOT)land_lad/land_types.F90
	cp $(SRCROOT)land_lad/land_types.F90 .
./compute_cpsi3.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/compute_cpsi3.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/compute_cpsi3.F90 .
./isccp_cloud_types.f: $(SRCROOT)atmos_param/cosp/icarus-scops-3.7/isccp_cloud_types.f
	cp $(SRCROOT)atmos_param/cosp/icarus-scops-3.7/isccp_cloud_types.f .
./cosp_io.f90: $(SRCROOT)atmos_param/cosp/cosp_io.f90
	cp $(SRCROOT)atmos_param/cosp/cosp_io.f90 .
./mosaic_util.c: $(SRCROOT)shared/mosaic/mosaic_util.c
	cp $(SRCROOT)shared/mosaic/mosaic_util.c .
./cmue_b.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/cmue_b.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/cmue_b.F90 .
./rdparm.F90: $(SRCROOT)atmos_param/fsrad/rdparm.F90
	cp $(SRCROOT)atmos_param/fsrad/rdparm.F90 .
./generic_BLING.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/ocean_shared/generic_tracers/generic_BLING.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/ocean_shared/generic_tracers/generic_BLING.F90 .
./ocean_sponges_tracer.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_sponges_tracer.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_sponges_tracer.F90 .
./rh_based_clouds.F90: $(SRCROOT)atmos_param/sea_esf_rad/rh_based_clouds.F90
	cp $(SRCROOT)atmos_param/sea_esf_rad/rh_based_clouds.F90 .
./cosp_stats.f90: $(SRCROOT)atmos_param/cosp/cosp_stats.f90
	cp $(SRCROOT)atmos_param/cosp/cosp_stats.f90 .
./ocean_vert_kpp.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_vert_kpp.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_vert_kpp.F90 .
./mask.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/ice_sis/mask.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/ice_sis/mask.F90 .
./pmaxmin.F90: $(SRCROOT)atmos_fv_dynamics/tools/pmaxmin.F90
	cp $(SRCROOT)atmos_fv_dynamics/tools/pmaxmin.F90 .
./donner_nml.h: /home/wenchang/scratch/tiger3/MOM4.1/src/atmos_param/donner_deep/donner_nml.h
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/atmos_param/donner_deep/donner_nml.h .
./constants.F90: $(SRCROOT)shared/constants/constants.F90
	cp $(SRCROOT)shared/constants/constants.F90 .
./longwave_driver.F90: $(SRCROOT)atmos_param/sea_esf_rad/longwave_driver.F90
	cp $(SRCROOT)atmos_param/sea_esf_rad/longwave_driver.F90 .
./dry_adj.F90: $(SRCROOT)atmos_param/dry_adj/dry_adj.F90
	cp $(SRCROOT)atmos_param/dry_adj/dry_adj.F90 .
./topography.F90: $(SRCROOT)shared/topography/topography.F90
	cp $(SRCROOT)shared/topography/topography.F90 .
./mpp_data_mpi.inc: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_data_mpi.inc
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_data_mpi.inc .
./radiation_driver.F90: $(SRCROOT)atmos_param/radiation_driver/radiation_driver.F90
	cp $(SRCROOT)atmos_param/radiation_driver/radiation_driver.F90 .
./mapz_module.F90: $(SRCROOT)atmos_fv_dynamics/model/mapz_module.F90
	cp $(SRCROOT)atmos_fv_dynamics/model/mapz_module.F90 .
./ocean_bgc_restore.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_bgc/ocean_bgc_restore.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_bgc/ocean_bgc_restore.F90 .
./quicksort.F90: $(SRCROOT)shared/drifters/quicksort.F90
	cp $(SRCROOT)shared/drifters/quicksort.F90 .
./mo_usrrxt.F90: $(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_usrrxt.F90
	cp $(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_usrrxt.F90 .
./rh_clouds.F90: $(SRCROOT)atmos_param/rh_clouds/rh_clouds.F90
	cp $(SRCROOT)atmos_param/rh_clouds/rh_clouds.F90 .
./gas_tf.F90: $(SRCROOT)atmos_param/sea_esf_rad/gas_tf.F90
	cp $(SRCROOT)atmos_param/sea_esf_rad/gas_tf.F90 .
./cosp_radar.f90: $(SRCROOT)atmos_param/cosp/llnl/cosp_radar.f90
	cp $(SRCROOT)atmos_param/cosp/llnl/cosp_radar.f90 .
./pf_to_mr.f: $(SRCROOT)atmos_param/cosp/llnl/pf_to_mr.f
	cp $(SRCROOT)atmos_param/cosp/llnl/pf_to_mr.f .
./ocean_convect.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_convect.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_convect.F90 .
./strat_chem_utilities.F90: $(SRCROOT)atmos_shared/tracer_driver/tropchem/strat_chem_utilities.F90
	cp $(SRCROOT)atmos_shared/tracer_driver/tropchem/strat_chem_utilities.F90 .
./array_lib.f90: $(SRCROOT)atmos_param/cosp/quickbeam/array_lib.f90
	cp $(SRCROOT)atmos_param/cosp/quickbeam/array_lib.f90 .
./mpp_domains_reduce.inc: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_domains_reduce.inc
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_domains_reduce.inc .
./conv_plumes_k.F90: $(SRCROOT)atmos_param/shallow_cu/conv_plumes_k.F90
	cp $(SRCROOT)atmos_param/shallow_cu/conv_plumes_k.F90 .
./tridiagonal_gotm.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/tridiagonal_gotm.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/tridiagonal_gotm.F90 .
./write_data.inc: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/fms/write_data.inc
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/fms/write_data.inc .
./moistproc_kernels.F90: $(SRCROOT)atmos_param/moist_processes/moistproc_kernels.F90
	cp $(SRCROOT)atmos_param/moist_processes/moistproc_kernels.F90 .
./ocean_nphysicsA.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_nphysicsA.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_nphysicsA.F90 .
./ocean_rough.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/ice_param/ocean_rough.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/ice_param/ocean_rough.F90 .
./mpp_do_update.h: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_do_update.h
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_do_update.h .
./congvec.inc: /home/wenchang/scratch/tiger3/MOM4.1/src/atmos_param/cosp/icarus-scops-3.7/congvec.inc
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/atmos_param/cosp/icarus-scops-3.7/congvec.inc .
./lw_gases_stdtf.F90: $(SRCROOT)atmos_param/sea_esf_rad/lw_gases_stdtf.F90
	cp $(SRCROOT)atmos_param/sea_esf_rad/lw_gases_stdtf.F90 .
./ocean_submesoscale.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_submesoscale.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_submesoscale.F90 .
./numerics.F90: $(SRCROOT)land_lad/numerics.F90
	cp $(SRCROOT)land_lad/numerics.F90 .
./mcm_sw_driver.F90: $(SRCROOT)atmos_param/fsrad/mcm_sw_driver.F90
	cp $(SRCROOT)atmos_param/fsrad/mcm_sw_driver.F90 .
./mpp_reduce_mpi.h: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_reduce_mpi.h
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_reduce_mpi.h .
./mpp_sum_mpi.h: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_sum_mpi.h
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_sum_mpi.h .
./mpp_io_read.inc: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_io_read.inc
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_io_read.inc .
./diag_cloud_rad.F90: $(SRCROOT)atmos_param/diag_cloud_rad/diag_cloud_rad.F90
	cp $(SRCROOT)atmos_param/diag_cloud_rad/diag_cloud_rad.F90 .
./ocmip2_biotic.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_bgc/ocmip2_biotic.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_bgc/ocmip2_biotic.F90 .
./ocean_tracer.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_tracer.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_tracer.F90 .
./MISR_simulator.f: $(SRCROOT)atmos_param/cosp/MISR_simulator/MISR_simulator.f
	cp $(SRCROOT)atmos_param/cosp/MISR_simulator/MISR_simulator.f .
./m_tracname.F90: $(SRCROOT)atmos_shared/tracer_driver/tropchem/m_tracname.F90
	cp $(SRCROOT)atmos_shared/tracer_driver/tropchem/m_tracname.F90 .
./vert_turb_driver.F90: $(SRCROOT)atmos_param/vert_turb_driver/vert_turb_driver.F90
	cp $(SRCROOT)atmos_param/vert_turb_driver/vert_turb_driver.F90 .
./bm_massflux.F90: $(SRCROOT)atmos_param/betts_miller/bm_massflux.F90
	cp $(SRCROOT)atmos_param/betts_miller/bm_massflux.F90 .
./horiz_interp.F90: $(SRCROOT)shared/horiz_interp/horiz_interp.F90
	cp $(SRCROOT)shared/horiz_interp/horiz_interp.F90 .
./create_xgrid.c: $(SRCROOT)shared/mosaic/create_xgrid.c
	cp $(SRCROOT)shared/mosaic/create_xgrid.c .
./mpp_do_updateV.h: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_do_updateV.h
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_do_updateV.h .
./atmos_tracer_utilities.F90: $(SRCROOT)atmos_shared/tracer_driver/atmos_tracer_utilities.F90
	cp $(SRCROOT)atmos_shared/tracer_driver/atmos_tracer_utilities.F90 .
./mpp_io_util.inc: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_io_util.inc
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_io_util.inc .
./ocean_nphysicsB.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_nphysicsB.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_nphysicsB.F90 .
./ocean_residency_range.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_residency_range.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_residency_range.F90 .
./lin_cloud_microphys.F90: $(SRCROOT)atmos_param/lin_cloud_microphys/lin_cloud_microphys.F90
	cp $(SRCROOT)atmos_param/lin_cloud_microphys/lin_cloud_microphys.F90 .
./ice_spec.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/ice_sis/ice_spec.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/ice_sis/ice_spec.F90 .
./field_manager.F90: $(SRCROOT)shared/field_manager/field_manager.F90
	cp $(SRCROOT)shared/field_manager/field_manager.F90 .
./cu_mo_trans.F90: $(SRCROOT)atmos_param/cu_mo_trans/cu_mo_trans.F90
	cp $(SRCROOT)atmos_param/cu_mo_trans/cu_mo_trans.F90 .
./mpp_sum_nocomm.h: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_sum_nocomm.h
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_sum_nocomm.h .
./fm_util.F90: $(SRCROOT)shared/field_manager/fm_util.F90
	cp $(SRCROOT)shared/field_manager/fm_util.F90 .
./mgrp_prscr_clds.F90: $(SRCROOT)atmos_param/sea_esf_rad/mgrp_prscr_clds.F90
	cp $(SRCROOT)atmos_param/sea_esf_rad/mgrp_prscr_clds.F90 .
./mpp_transmit_sma.h: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_transmit_sma.h
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_transmit_sma.h .
./moist_conv.F90: $(SRCROOT)atmos_param/moist_conv/moist_conv.F90
	cp $(SRCROOT)atmos_param/moist_conv/moist_conv.F90 .
./mpp_do_global_field.h: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_do_global_field.h
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_do_global_field.h .
./pv_module.F90: $(SRCROOT)atmos_fv_dynamics/tools/pv_module.F90
	cp $(SRCROOT)atmos_fv_dynamics/tools/pv_module.F90 .
./column_diagnostics.F90: $(SRCROOT)shared/column_diagnostics/column_diagnostics.F90
	cp $(SRCROOT)shared/column_diagnostics/column_diagnostics.F90 .
./generic_CFC.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/ocean_shared/generic_tracers/generic_CFC.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/ocean_shared/generic_tracers/generic_CFC.F90 .
./optical_path.F90: $(SRCROOT)atmos_param/sea_esf_rad/optical_path.F90
	cp $(SRCROOT)atmos_param/sea_esf_rad/optical_path.F90 .
./donner_cape_k.F90: $(SRCROOT)atmos_param/donner_deep/donner_cape_k.F90
	cp $(SRCROOT)atmos_param/donner_deep/donner_cape_k.F90 .
./mo_rodas_slv.F90: $(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_rodas_slv.F90
	cp $(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_rodas_slv.F90 .
./diag_util.F90: $(SRCROOT)shared/diag_manager/diag_util.F90
	cp $(SRCROOT)shared/diag_manager/diag_util.F90 .
./cg_drag.F90: $(SRCROOT)atmos_param/cg_drag/cg_drag.F90
	cp $(SRCROOT)atmos_param/cg_drag/cg_drag.F90 .
./memuse.c: $(SRCROOT)shared/memutils/memuse.c
	cp $(SRCROOT)shared/memutils/memuse.c .
./co2_data.F90: $(SRCROOT)atmos_param/fsrad/co2_data.F90
	cp $(SRCROOT)atmos_param/fsrad/co2_data.F90 .
./time.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/time.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/time.F90 .
./optics_lib.f90: $(SRCROOT)atmos_param/cosp/quickbeam/optics_lib.f90
	cp $(SRCROOT)atmos_param/cosp/quickbeam/optics_lib.f90 .
./topo_drag.F90: $(SRCROOT)atmos_param/topo_drag/topo_drag.F90
	cp $(SRCROOT)atmos_param/topo_drag/topo_drag.F90 .
./gradient_c2l.c: $(SRCROOT)shared/mosaic/gradient_c2l.c
	cp $(SRCROOT)shared/mosaic/gradient_c2l.c .
./mpp_util_mpi.inc: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_util_mpi.inc
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_util_mpi.inc .
./ocean_vert_chen.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_vert_chen.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_vert_chen.F90 .
./util.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/util.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/util.F90 .
./ocean_albedo.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/ice_param/ocean_albedo.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/ice_param/ocean_albedo.F90 .
./damping_driver.F90: $(SRCROOT)atmos_param/damping_driver/damping_driver.F90
	cp $(SRCROOT)atmos_param/damping_driver/damping_driver.F90 .
./strat_chem_model.F90: $(SRCROOT)atmos_shared/tracer_driver/stratchem/strat_chem_model.F90
	cp $(SRCROOT)atmos_shared/tracer_driver/stratchem/strat_chem_model.F90 .
./ocean_rivermix.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_rivermix.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_rivermix.F90 .
./diag_integral.F90: $(SRCROOT)atmos_param/diag_integral/diag_integral.F90
	cp $(SRCROOT)atmos_param/diag_integral/diag_integral.F90 .
./mpp_sum.inc: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_sum.inc
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_sum.inc .
./sat_vapor_pres_k.F90: $(SRCROOT)shared/sat_vapor_pres/sat_vapor_pres_k.F90
	cp $(SRCROOT)shared/sat_vapor_pres/sat_vapor_pres_k.F90 .
./generic_tracer_utils.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/ocean_shared/generic_tracers/generic_tracer_utils.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/ocean_shared/generic_tracers/generic_tracer_utils.F90 .
./original_fms_rad.F90: $(SRCROOT)atmos_param/sea_esf_rad/original_fms_rad.F90
	cp $(SRCROOT)atmos_param/sea_esf_rad/original_fms_rad.F90 .
./prec_scops.f: $(SRCROOT)atmos_param/cosp/llnl/prec_scops.f
	cp $(SRCROOT)atmos_param/cosp/llnl/prec_scops.f .
./gradient_c2l.h: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mosaic/gradient_c2l.h
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mosaic/gradient_c2l.h .
./drifters_set_field.h: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/drifters/drifters_set_field.h
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/drifters/drifters_set_field.h .
./ocean_vert_tidal.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_vert_tidal.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_vert_tidal.F90 .
./drifters_io.F90: $(SRCROOT)shared/drifters/drifters_io.F90
	cp $(SRCROOT)shared/drifters/drifters_io.F90 .
./mpp_memutils.F90: $(SRCROOT)shared/mpp/mpp_memutils.F90
	cp $(SRCROOT)shared/mpp/mpp_memutils.F90 .
./stable_bl_turb.F90: $(SRCROOT)atmos_param/stable_bl_turb/stable_bl_turb.F90
	cp $(SRCROOT)atmos_param/stable_bl_turb/stable_bl_turb.F90 .
./donner_lscloud_k.F90: $(SRCROOT)atmos_param/donner_deep/donner_lscloud_k.F90
	cp $(SRCROOT)atmos_param/donner_deep/donner_lscloud_k.F90 .
./upper.F90: $(SRCROOT)atmos_fv_dynamics/tools/upper.F90
	cp $(SRCROOT)atmos_fv_dynamics/tools/upper.F90 .
./FMS_ocmip2_co2calc.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/ocean_shared/generic_tracers/FMS_ocmip2_co2calc.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/ocean_shared/generic_tracers/FMS_ocmip2_co2calc.F90 .
./nonfms_donner.F90: $(SRCROOT)atmos_param/donner_deep/nonfms_donner.F90
	cp $(SRCROOT)atmos_param/donner_deep/nonfms_donner.F90 .
./convert_fluxes.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/convert_fluxes.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/convert_fluxes.F90 .
./mpp_comm_nocomm.inc: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_comm_nocomm.inc
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_comm_nocomm.inc .
./mo_jpl.F90: $(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_jpl.F90
	cp $(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_jpl.F90 .
./ocean_overexchange.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_overexchange.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_overexchange.F90 .
./ice_bergs.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/ice_sis/ice_bergs.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/ice_sis/ice_bergs.F90 .
./ocean_tpm.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_tpm.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_tpm.F90 .
./mo_exp_slv.F90: $(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_exp_slv.F90
	cp $(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_exp_slv.F90 .
./ensemble_manager.F90: $(SRCROOT)shared/coupler/ensemble_manager.F90
	cp $(SRCROOT)shared/coupler/ensemble_manager.F90 .
./fv_arrays.h: /home/wenchang/scratch/tiger3/MOM4.1/src/atmos_fv_dynamics/model/fv_arrays.h
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/atmos_fv_dynamics/model/fv_arrays.h .
./ozone.F90: $(SRCROOT)atmos_param/sea_esf_rad/ozone.F90
	cp $(SRCROOT)atmos_param/sea_esf_rad/ozone.F90 .
./mpp_util.inc: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_util.inc
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_util.inc .
./fv_restart.F90: $(SRCROOT)atmos_fv_dynamics/tools/fv_restart.F90
	cp $(SRCROOT)atmos_fv_dynamics/tools/fv_restart.F90 .
./ocean_nphysics.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_nphysics.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_nphysics.F90 .
./fms_platform.h: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/include/fms_platform.h
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/include/fms_platform.h .
./aer_in_act.F90: $(SRCROOT)atmos_shared/tracer_driver/aer_ccn_act/aer_in_act.F90
	cp $(SRCROOT)atmos_shared/tracer_driver/aer_ccn_act/aer_in_act.F90 .
./aer_ccn_act.F90: $(SRCROOT)atmos_shared/tracer_driver/aer_ccn_act/aer_ccn_act.F90
	cp $(SRCROOT)atmos_shared/tracer_driver/aer_ccn_act/aer_ccn_act.F90 .
./radar_simulator_types.f90: $(SRCROOT)atmos_param/cosp/quickbeam/radar_simulator_types.f90
	cp $(SRCROOT)atmos_param/cosp/quickbeam/radar_simulator_types.f90 .
./mpp_io_write.inc: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_io_write.inc
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_io_write.inc .
./mcm_swtbls.F90: $(SRCROOT)atmos_param/fsrad/mcm_swtbls.F90
	cp $(SRCROOT)atmos_param/fsrad/mcm_swtbls.F90 .
./shallow_conv.F90: $(SRCROOT)atmos_param/shallow_conv/shallow_conv.F90
	cp $(SRCROOT)atmos_param/shallow_conv/shallow_conv.F90 .
./longwave_clouds.F90: $(SRCROOT)atmos_param/sea_esf_rad/longwave_clouds.F90
	cp $(SRCROOT)atmos_param/sea_esf_rad/longwave_clouds.F90 .
./lengthscaleeq.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/lengthscaleeq.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/lengthscaleeq.F90 .
./fk_craig.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/fk_craig.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/fk_craig.F90 .
./mpp_update_domains2D.h: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_update_domains2D.h
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_update_domains2D.h .
./mpp_write_2Ddecomp.h: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_write_2Ddecomp.h
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_write_2Ddecomp.h .
./ocean_increment_eta.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_increment_eta.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_increment_eta.F90 .
./gotm_lib_version.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/gotm_lib_version.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/gotm_lib_version.F90 .
./threadloc.c: $(SRCROOT)shared/mpp/threadloc.c
	cp $(SRCROOT)shared/mpp/threadloc.c .
./zetac_clouds_W.F90: $(SRCROOT)atmos_param/sea_esf_rad/zetac_clouds_W.F90
	cp $(SRCROOT)atmos_param/sea_esf_rad/zetac_clouds_W.F90 .
./ocean_grids.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_grids.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_grids.F90 .
./generic_TOPAZ.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/ocean_shared/generic_tracers/generic_TOPAZ.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/ocean_shared/generic_tracers/generic_TOPAZ.F90 .
./ocean_increment_velocity.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_increment_velocity.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_increment_velocity.F90 .
./ocean_shortwave.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_shortwave.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_shortwave.F90 .
./ocean_po4_pre.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_bgc/ocean_po4_pre.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_bgc/ocean_po4_pre.F90 .
./isccp_clouds.F90: $(SRCROOT)atmos_param/sea_esf_rad/isccp_clouds.F90
	cp $(SRCROOT)atmos_param/sea_esf_rad/isccp_clouds.F90 .
./r_ratio.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/r_ratio.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/r_ratio.F90 .
./ocean_ibgc.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_bgc/ocean_ibgc.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_bgc/ocean_ibgc.F90 .
./microphys_cloud.F90: $(SRCROOT)atmos_param/sea_esf_rad/microphys_cloud.F90
	cp $(SRCROOT)atmos_param/sea_esf_rad/microphys_cloud.F90 .
./mpp_domains_misc.inc: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_domains_misc.inc
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_domains_misc.inc .
./mpp_utilities.F90: $(SRCROOT)shared/mpp/mpp_utilities.F90
	cp $(SRCROOT)shared/mpp/mpp_utilities.F90 .
./ocean_bbc.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_bbc.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_bbc.F90 .
./cosp_utils.f90: $(SRCROOT)atmos_param/cosp/cosp_utils.f90
	cp $(SRCROOT)atmos_param/cosp/cosp_utils.f90 .
./mpp_domains.F90: $(SRCROOT)shared/mpp/mpp_domains.F90
	cp $(SRCROOT)shared/mpp/mpp_domains.F90 .
./mpp_comm_sma.inc: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_comm_sma.inc
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_comm_sma.inc .
./ocean_util.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_util.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_util.F90 .
./my25_turb.F90: $(SRCROOT)atmos_param/my25_turb/my25_turb.F90
	cp $(SRCROOT)atmos_param/my25_turb/my25_turb.F90 .
./tkealgebraic.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/tkealgebraic.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/tkealgebraic.F90 .
./fsrad.F90: $(SRCROOT)atmos_param/fsrad/fsrad.F90
	cp $(SRCROOT)atmos_param/fsrad/fsrad.F90 .
./ice_grid.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/ice_sis/ice_grid.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/ice_sis/ice_grid.F90 .
./mpp_error_s_s.h: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_error_s_s.h
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_error_s_s.h .
./atmos_dust.F90: $(SRCROOT)atmos_shared/tracer_driver/atmos_dust.F90
	cp $(SRCROOT)atmos_shared/tracer_driver/atmos_dust.F90 .
./atmos_sulfate.F90: $(SRCROOT)atmos_shared/tracer_driver/atmos_sulfate.F90
	cp $(SRCROOT)atmos_shared/tracer_driver/atmos_sulfate.F90 .
./ocean_time_filter.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_time_filter.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_time_filter.F90 .
./mpp_do_get_boundary.h: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_do_get_boundary.h
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_do_get_boundary.h .
./tracer_2d.F90: $(SRCROOT)atmos_fv_dynamics/model/tracer_2d.F90
	cp $(SRCROOT)atmos_fv_dynamics/model/tracer_2d.F90 .
./shallow_physics.F90: $(SRCROOT)atmos_param/shallow_physics/shallow_physics.F90
	cp $(SRCROOT)atmos_param/shallow_physics/shallow_physics.F90 .
./vert_diff_driver.F90: $(SRCROOT)atmos_param/vert_diff_driver/vert_diff_driver.F90
	cp $(SRCROOT)atmos_param/vert_diff_driver/vert_diff_driver.F90 .
./read_data_3d.inc: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/fms/read_data_3d.inc
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/fms/read_data_3d.inc .
./ice_type.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/ice_sis/ice_type.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/ice_sis/ice_type.F90 .
./diag_grid.F90: $(SRCROOT)shared/diag_manager/diag_grid.F90
	cp $(SRCROOT)shared/diag_manager/diag_grid.F90 .
./ocean_types.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_types.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_types.F90 .
./mpp_domains_define.inc: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_domains_define.inc
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_domains_define.inc .
./ocean_bih_friction.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_bih_friction.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_bih_friction.F90 .
./cmue_ma.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/cmue_ma.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/cmue_ma.F90 .
./mpp_transmit.inc: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_transmit.inc
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_transmit.inc .
./station_data.F90: $(SRCROOT)shared/station_data/station_data.F90
	cp $(SRCROOT)shared/station_data/station_data.F90 .
./cosp_misr_simulator.f90: $(SRCROOT)atmos_param/cosp/cosp_misr_simulator.f90
	cp $(SRCROOT)atmos_param/cosp/cosp_misr_simulator.f90 .
./atmos_model.F90: $(SRCROOT)atmos_coupled/atmos_model.F90
	cp $(SRCROOT)atmos_coupled/atmos_model.F90 .
./oda_driver.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/oda_driver.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/oda_driver.F90 .
./ocean_residency_meta.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_residency_meta.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_residency_meta.F90 .
./mpp_reduce_sma.h: /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_reduce_sma.h
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_reduce_sma.h .
./oda_core.F90: $(SRCROOT)shared/oda_tools/oda_core.F90
	cp $(SRCROOT)shared/oda_tools/oda_core.F90 .
./time_interp_external.F90: $(SRCROOT)shared/time_interp/time_interp_external.F90
	cp $(SRCROOT)shared/time_interp/time_interp_external.F90 .
./ocean_residency_integrand.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_residency_integrand.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_residency_integrand.F90 .
./shortwave.F90: $(SRCROOT)atmos_param/fsrad/shortwave.F90
	cp $(SRCROOT)atmos_param/fsrad/shortwave.F90 .
./ocean_generic_tracer.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_bgc/ocean_generic_tracer.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_bgc/ocean_generic_tracer.F90 .
./ocean_bihgen_friction.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_bihgen_friction.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_bihgen_friction.F90 .
./xgrid.F90: $(SRCROOT)shared/exchange/xgrid.F90
	cp $(SRCROOT)shared/exchange/xgrid.F90 .
./internal_wave.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/internal_wave.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/internal_wave.F90 .
./lhsw_driver.F90: $(SRCROOT)atmos_param/sea_esf_rad/lhsw_driver.F90
	cp $(SRCROOT)atmos_param/sea_esf_rad/lhsw_driver.F90 .
./ice_thm.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/ice_sis/ice_thm.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/ice_sis/ice_thm.F90 .
./cmue_a.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/cmue_a.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/cmue_a.F90 .
./potentialml.F90: /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/potentialml.F90
	cp /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/potentialml.F90 .
./tp_core.F90: $(SRCROOT)atmos_fv_dynamics/model/tp_core.F90
	cp $(SRCROOT)atmos_fv_dynamics/model/tp_core.F90 .
SRC = $(SRCROOT)atmos_param/physics_driver/physics_driver.F90 $(SRCROOT)shared/data_override/data_override.F90 $(SRCROOT)shared/random_numbers/random_numbers.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_grids.F90                   \
$(SRCROOT)shared/oda_tools/write_ocean_data.F90 $(SRCROOT)atmos_param/cosp/actsim/lmd_ipsl_stats.f90 $(SRCROOT)atmos_param/donner_deep/cumulus_closure_k.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_bgc/ocmip2_biotic.F90                       \
$(SRCROOT)atmos_param/shallow_cu/uw_conv.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/oda_driver.F90 $(SRCROOT)atmos_param/rh_clouds/rh_clouds.F90 $(SRCROOT)atmos_param/fsrad/longwave.F90 $(SRCROOT)shared/diag_manager/diag_output.F90    \
$(SRCROOT)shared/drifters/cloud_interpolator.F90 $(SRCROOT)shared/fft/fft99.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_tpm.F90 $(SRCROOT)atmos_param/cosp/cosp_stats.f90 $(SRCROOT)atmos_param/donner_deep/donner_deep_k.F90      \
$(SRCROOT)atmos_param/sea_esf_rad/donner_deep_clouds_W.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_residency_ml.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_bgc/ocean_bgc_restore.F90                                \
$(SRCROOT)atmos_param/sea_esf_rad/sealw99.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_shortwave_gfdl.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/kbeq.F90                            \
$(SRCROOT)atmos_param/cloud_rad/cloud_rad.F90 $(SRCROOT)atmos_param/sea_esf_rad/uw_clouds_W.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/ocean_shared/generic_tracers/generic_tracer_utils.F90 $(SRCROOT)atmos_shared/tracer_driver/atmos_tracer_utilities.F90 \
$(SRCROOT)shared/constants/constants.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_lapgen_friction.F90 $(SRCROOT)land_param/climap_albedo.F90                                                                                   \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_nphysics_util.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/ice_sis/ice_dyn.F90 $(SRCROOT)atmos_param/sea_esf_rad/standalone_clouds.F90 $(SRCROOT)land_lad/soil/rivers.F90             \
$(SRCROOT)atmos_param/donner_deep/wet_deposition_0D.F90 $(SRCROOT)atmos_param/cosp/llnl/llnl_stats.f90 $(SRCROOT)atmos_shared/tracer_driver/atmos_age_tracer.F90 $(SRCROOT)shared/topography/topography.F90 $(SRCROOT)shared/mpp/nsclock.c                     \
$(SRCROOT)shared/mosaic/interp.c $(SRCROOT)atmos_param/cosp/actsim/lidar_simulator.f90 $(SRCROOT)shared/sat_vapor_pres/sat_vapor_pres_k.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/potentialml.F90                    \
$(SRCROOT)atmos_shared/tracer_driver/atmos_dust.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/ocean_shared/generic_tracers/FMS_ocmip2_co2calc.F90 $(SRCROOT)atmos_param/sea_esf_rad/zetac_clouds_W.F90 $(SRCROOT)shared/oda_tools/oda_types.F90                 \
$(SRCROOT)atmos_param/cosp/cosp_constants.f90 $(SRCROOT)atmos_param/moist_processes/moistproc_kernels.F90 $(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_chemini.F90                                                                                         \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_sigma_transport.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_overflow.F90                                                                            \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/compute_rist.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_model.F90 $(SRCROOT)atmos_param/donner_deep/donner_utilities_k.F90                           \
$(SRCROOT)atmos_param/cosp/quickbeam/array_lib.f90 $(SRCROOT)shared/oda_tools/oda_core.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/cmue_rf.F90                                                                         \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_diag/ocean_diagnostics.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_form_drag.F90 $(SRCROOT)atmos_param/donner_deep/donner_lscloud_k.F90                                 \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_thickness.F90 $(SRCROOT)atmos_shared/interpolator/interpolator.F90 $(SRCROOT)shared/coupler/coupler_types.F90                                                                                 \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_diag/ocean_velocity_diag.F90 $(SRCROOT)atmos_param/monin_obukhov/monin_obukhov_kernel.F90 $(SRCROOT)atmos_param/fsrad/mcm_sw_driver.F90 $(SRCROOT)shared/mpp/mpp.F90                                     \
$(SRCROOT)atmos_fv_dynamics/driver/coupled/atmosphere.F90 $(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_hook.F90 $(SRCROOT)atmos_param/cosp/cosp_lidar.f90 $(SRCROOT)shared/mpp/mpp_utilities.F90 $(SRCROOT)atmos_param/shallow_physics/shallow_physics.F90 \
$(SRCROOT)atmos_fv_dynamics/tools/mod_comm.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_frazil.F90 $(SRCROOT)atmos_fv_dynamics/model/fill_module.F90 $(SRCROOT)atmos_param/cosp/llnl/pf_to_mr.f                                     \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/util.F90 $(SRCROOT)land_lad/soil/soil.F90 $(SRCROOT)atmos_param/donner_deep/donner_cape_k.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_nphysicsA.F90 \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/ode_solvers.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_bihcst_friction.F90 $(SRCROOT)atmos_shared/tracer_driver/tropchem/moz.subs.F90              \
$(SRCROOT)shared/mpp/mpp_parameter.F90 $(SRCROOT)atmos_param/cosp/MISR_simulator/MISR_simulator.f $(SRCROOT)shared/axis_utils/axis_utils.F90 $(SRCROOT)atmos_param/sea_esf_rad/isccp_clouds.F90                                                                \
/home/wenchang/scratch/tiger3/MOM4.1/src/ice_param/ocean_rough.F90 $(SRCROOT)atmos_fv_dynamics/tools/init_dry_atm.F90 $(SRCROOT)atmos_param/cosp/quickbeam/load_hydrometeor_classes.f90 $(SRCROOT)shared/mpp/mpp_io.F90                                        \
$(SRCROOT)atmos_param/vert_turb_driver/vert_turb_driver.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/adv_center.F90 $(SRCROOT)atmos_param/dry_adj/dry_adj.F90 $(SRCROOT)atmos_fv_dynamics/tools/gmean.F90                     \
$(SRCROOT)atmos_fv_dynamics/model/tracer_2d.F90 $(SRCROOT)atmos_param/fsrad/co2int.F90 $(SRCROOT)atmos_param/sea_esf_rad/bulkphys_rad.F90 $(SRCROOT)atmos_param/sea_esf_rad/strat_clouds_W.F90 $(SRCROOT)atmos_fv_dynamics/model/shr_kind_mod.F90              \
$(SRCROOT)atmos_fv_dynamics/tools/timingModule.F90 $(SRCROOT)atmos_param/diag_cloud_rad/diag_cloud_rad.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_util.F90 $(SRCROOT)atmos_param/topo_drag/topo_drag.F90                             \
$(SRCROOT)shared/horiz_interp/horiz_interp_conserve.F90 $(SRCROOT)atmos_param/cu_mo_trans/cu_mo_trans.F90 $(SRCROOT)atmos_param/lin_cloud_microphys/lin_cloud_microphys.F90                                                                                    \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_xlandinsert.F90 $(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_chemdr.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_rivermix.F90                   \
$(SRCROOT)atmos_param/monin_obukhov/monin_obukhov.F90 $(SRCROOT)atmos_param/mg_drag/mg_drag.F90 $(SRCROOT)shared/drifters/drifters_comm.F90 $(SRCROOT)atmos_param/fsrad/shortwave.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/ice_param/ocean_albedo.F90      \
$(SRCROOT)atmos_param/cosp/quickbeam/load_mie_table.f90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_velocity.F90 $(SRCROOT)atmos_param/cosp/quickbeam/atmos_lib.f90                                                                       \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_increment_velocity.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/ocean_shared/generic_tracers/generic_BLING.F90 $(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_imp_slv.F90          \
$(SRCROOT)atmos_param/fsrad/mcm_swtbls.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_sponges_eta.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_residency_meta.F90                                    \
$(SRCROOT)atmos_param/clouds/clouds.F90 $(SRCROOT)shared/mosaic/read_mosaic.c $(SRCROOT)shared/fms/fms_io.F90 $(SRCROOT)atmos_param/fsrad/mcm_swnew.F90 $(SRCROOT)atmos_fv_dynamics/tools/upper.F90 $(SRCROOT)atmos_param/sea_esf_rad/optical_path.F90         \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_types.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_residency.F90 $(SRCROOT)atmos_param/cosp/quickbeam/radar_simulator_types.f90                                    \
$(SRCROOT)atmos_shared/tracer_driver/aer_ccn_act/aer_ccn_act_k.F90 $(SRCROOT)atmos_fv_dynamics/tools/pv_module.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/gridinterpol.F90                                                  \
$(SRCROOT)atmos_param/cosp/icarus-scops-3.7/scops.f /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/lagrange.F90 $(SRCROOT)shared/time_interp/time_interp.F90 $(SRCROOT)atmos_param/sea_esf_rad/longwave_tables.F90                  \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_nphysicsC.F90 $(SRCROOT)atmos_param/sea_esf_rad/specified_clouds_W.F90 $(SRCROOT)atmos_shared/tracer_driver/atmos_co2.F90                                                             \
/home/wenchang/scratch/tiger3/MOM4.1/src/coupler/coupler_main.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_momentum_source.F90 $(SRCROOT)shared/topography/gaussian_topog.F90 $(SRCROOT)shared/memutils/memutils.F90          \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/cmue_ma.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/ocean_shared/generic_tracers/generic_CFC.F90 $(SRCROOT)atmos_param/donner_deep/nonfms_donner.F90                          \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/cmue_b.F90 $(SRCROOT)atmos_shared/tracer_driver/atmos_carbon_aerosol.F90 $(SRCROOT)atmos_fv_dynamics/tools/getmax.F90 $(SRCROOT)shared/fms/fms.F90                             \
$(SRCROOT)atmos_param/cosp/cosp_io.f90 $(SRCROOT)atmos_param/sea_esf_rad/cloudrad_diagnostics.F90 $(SRCROOT)atmos_param/donner_deep/fms_donner.F90 $(SRCROOT)atmos_shared/atmos_nudge/atmos_nudge.F90                                                          \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_bgc/ocean_po4_pre.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_bbc.F90 $(SRCROOT)shared/diag_manager/diag_manager.F90 $(SRCROOT)atmos_param/shallow_cu/conv_utilities_k.F90      \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/variances.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_bgc/ocean_pert_co2.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_age_tracer.F90  \
$(SRCROOT)shared/tridiagonal/tridiagonal.F90 $(SRCROOT)atmos_param/diag_cloud/diag_cloud.F90 $(SRCROOT)shared/drifters/drifters_io.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_barotropic.F90 $(SRCROOT)land_lad/land_types.F90       \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_diag/ocean_tracer_diag.F90 $(SRCROOT)shared/mpp/mpp_domains.F90 $(SRCROOT)shared/diag_manager/diag_grid.F90 $(SRCROOT)atmos_coupled/atmos_model.F90                                                      \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_bgc/ocean_generic_tracer.F90 $(SRCROOT)shared/exchange/xgrid.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/ispralength.F90                                         \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_density.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/transport_matrix.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_xlandmix.F90         \
$(SRCROOT)shared/diag_manager/diag_data.F90 $(SRCROOT)atmos_param/sea_esf_rad/microphys_rad.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/tridiagonal_gotm.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/ice_sis/rot.F90        \
$(SRCROOT)atmos_shared/tracer_driver/atmos_soa.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_lap_friction.F90 $(SRCROOT)atmos_param/diffusivity/diffusivity.F90 $(SRCROOT)atmos_param/fsrad/mcm_lw.F90                          \
/home/wenchang/scratch/tiger3/MOM4.1/src/ice_sis/ice_model.F90 $(SRCROOT)shared/mosaic/gradient_c2l.c $(SRCROOT)atmos_param/strat_cloud/strat_cloud.F90 $(SRCROOT)land_lad/land_model.F90 $(SRCROOT)atmos_param/vert_diff/vert_diff.F90                        \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_sponges_velocity.F90 $(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_photo.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_bih_tracer.F90              \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/fk_craig.F90 $(SRCROOT)atmos_param/cosp/quickbeam/radar_simulator.f90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/q2over2eq.F90            \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/eqstate.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/ocean_shared/generic_tracers/generic_tracer.F90                                                                                 \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_vert_pp.F90 $(SRCROOT)atmos_shared/tracer_driver/tropchem/moz.mat.F90 $(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_usrrxt.F90 $(SRCROOT)atmos_param/shallow_cu/conv_plumes.F90    \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/gotm_lib_version.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/ice_sis/ice_spec.F90 $(SRCROOT)atmos_fv_dynamics/model/update_fv_phys.F90                                        \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_diag/ocean_adv_vel_diag.F90 $(SRCROOT)shared/platform/platform.F90 $(SRCROOT)shared/horiz_interp/horiz_interp_type.F90                                                                                   \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/cmue_sg.F90 $(SRCROOT)atmos_shared/tracer_driver/stratchem/strat_chem_model.F90 $(SRCROOT)atmos_param/moist_processes/moist_processes_utils.F90                                \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_increment_tracer.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_time_filter.F90 $(SRCROOT)atmos_param/sea_esf_rad/rh_based_clouds.F90                 \
$(SRCROOT)atmos_fv_dynamics/tools/init_sw_ic.F90 $(SRCROOT)shared/horiz_interp/horiz_interp_bicubic.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/coupler/surface_flux.F90 $(SRCROOT)atmos_param/sea_esf_rad/radiation_diag.F90                                 \
$(SRCROOT)atmos_shared/tracer_driver/atmos_sulfur_hex.F90 $(SRCROOT)atmos_param/betts_miller/bm_massflux.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/algebraiclength.F90                                               \
$(SRCROOT)atmos_fv_dynamics/model/dyn_core.F90 $(SRCROOT)atmos_param/fsrad/fsrad.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_tempsalt.F90 $(SRCROOT)shared/drifters/drifters.F90                                                   \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_bgc/ocmip2_he.F90 $(SRCROOT)atmos_fv_dynamics/tools/age_of_air.F90 $(SRCROOT)atmos_shared/vert_advection/vert_advection.F90 $(SRCROOT)shared/memutils/memuse.c                                           \
$(SRCROOT)atmos_param/shallow_cu/deep_conv.F90 $(SRCROOT)atmos_fv_dynamics/model/fv_pack.F90 $(SRCROOT)atmos_param/cloud_obs/cloud_obs.F90 $(SRCROOT)atmos_param/cosp/quickbeam/mrgrnk.f90                                                                     \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_bih_friction.F90 $(SRCROOT)atmos_param/shallow_conv/shallow_conv.F90 $(SRCROOT)atmos_fv_dynamics/model/fv_dynamics.F90 $(SRCROOT)atmos_param/lscale_cond/lscale_cond.F90              \
$(SRCROOT)shared/oda_tools/xbt_drop_rate_adjust.f90 $(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_setinv.F90 $(SRCROOT)atmos_shared/tracer_driver/atmos_tracer_driver.F90 $(SRCROOT)shared/mpp/threadloc.c                                                  \
$(SRCROOT)atmos_param/donner_deep/donner_cloud_model_k.F90 $(SRCROOT)atmos_param/sea_esf_rad/cloudrad_package.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/dissipationeq.F90                                            \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/tkeeq.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_workspace.F90                                                                                       \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_lap_tracer.F90 $(SRCROOT)shared/coupler/ensemble_manager.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_topog.F90 $(SRCROOT)shared/mosaic/gradient.F90          \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_polar_filter.F90 $(SRCROOT)atmos_param/cg_drag/cg_drag.F90 $(SRCROOT)atmos_param/cosp/llnl/prec_scops.f $(SRCROOT)atmos_param/fsrad/co2_data.F90                                     \
$(SRCROOT)atmos_param/donner_deep/donner_types.F90 $(SRCROOT)shared/drifters/drifters_input.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_pressure.F90 $(SRCROOT)shared/mpp/mpp_memutils.F90                                            \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_operators.F90 $(SRCROOT)atmos_param/moist_processes/moist_processes.F90 $(SRCROOT)atmos_param/entrain/entrain.F90                                                                             \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_diag/ocean_drifters.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_mixdownslope.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_vert_gotm.F90 \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/tkealgebraic.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/ice_sis/ice_thm.F90 $(SRCROOT)atmos_fv_dynamics/tools/par_vecsum.F90                                                 \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/cmue_c.F90 $(SRCROOT)atmos_shared/tracer_driver/atmos_radon.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/genericeq.F90                  \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/diff_center.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/r_ratio.F90 $(SRCROOT)shared/sat_vapor_pres/sat_vapor_pres.F90                       \
$(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_read_sim_chm.F90 $(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_chem_utls.F90 $(SRCROOT)atmos_param/sea_esf_rad/aerosol.F90 $(SRCROOT)atmos_shared/tracer_driver/tropchem/strat_chem_utilities.F90          \
$(SRCROOT)atmos_param/damping_driver/damping_driver.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_convect.F90 $(SRCROOT)atmos_param/cosp/cosp_isccp_simulator.f90 $(SRCROOT)atmos_param/donner_deep/donner_deep.F90             \
$(SRCROOT)shared/time_manager/time_manager.F90 $(SRCROOT)shared/exchange/stock_constants.F90 $(SRCROOT)atmos_param/sea_esf_rad/sea_esf_rad.F90 $(SRCROOT)atmos_param/sea_esf_rad/rad_utilities.F90 $(SRCROOT)atmos_param/diag_integral/diag_integral.F90       \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_parameters.F90 $(SRCROOT)atmos_param/cosp/icarus-scops-3.7/isccp_cloud_types.f $(SRCROOT)atmos_param/sea_esf_rad/longwave_fluxes.F90                                                          \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_nphysics.F90 $(SRCROOT)land_lad/numerics.F90 $(SRCROOT)atmos_fv_dynamics/model/pft_module.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/kpp.F90 \
$(SRCROOT)atmos_param/betts_miller/betts_miller.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_vert_tidal.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/ocean_shared/generic_tracers/generic_TOPAZ.F90                            \
$(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_setsox.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/cmue_d.F90 $(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_exp_slv.F90                                            \
$(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_jpl.F90 $(SRCROOT)atmos_shared/tracer_driver/tropchem/m_tracname.F90 $(SRCROOT)shared/diag_manager/diag_util.F90 $(SRCROOT)atmos_fv_dynamics/tools/fv_restart.F90                                             \
$(SRCROOT)atmos_param/sea_esf_rad/diag_clouds_W.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/compute_cpsi3.F90 $(SRCROOT)shared/random_numbers/MersenneTwister.F90                                                      \
$(SRCROOT)atmos_param/donner_deep/donner_deep_miz.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_velocity_advect.F90 $(SRCROOT)land_lad/soil/land_properties.F90 $(SRCROOT)atmos_param/fsrad/rdparm.F90                                  \
$(SRCROOT)atmos_param/sea_esf_rad/gas_tf.F90 $(SRCROOT)atmos_param/sea_esf_rad/lhsw_driver.F90 $(SRCROOT)atmos_shared/tracer_driver/stratchem/strat_chem_driver.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/ice_sis/ice_type.F90                              \
$(SRCROOT)atmos_param/fsrad/rad_diag.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_bgc/ocean_ibgc.F90 $(SRCROOT)shared/mosaic/create_xgrid.c /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/epsbalgebraic.F90     \
$(SRCROOT)shared/mpp/mpp_data.F90 $(SRCROOT)atmos_param/cosp/quickbeam/optics_lib.f90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_passive.F90                                                                                          \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_residency_integrand.F90 $(SRCROOT)atmos_shared/tracer_driver/aer_ccn_act/aer_in_act.F90 $(SRCROOT)atmos_param/sea_esf_rad/rad_output_file.F90 $(SRCROOT)atmos_fv_dynamics/model/ecmfft.F90 \
$(SRCROOT)atmos_param/cosp/cosp_utils.f90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_shortwave.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_sponges_tracer.F90                                 \
$(SRCROOT)atmos_param/donner_deep/donner_meso_k.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/kbalgebraic.F90 $(SRCROOT)atmos_param/moist_conv/moist_conv.F90 $(SRCROOT)atmos_param/cosp/quickbeam/dsd.f90               \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_bgc/ocmip2_abiotic.F90 $(SRCROOT)atmos_param/cosp/cosp_simulator.f90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/convert_fluxes.F90 $(SRCROOT)atmos_param/cosp/cosp.f90    \
$(SRCROOT)atmos_param/grey_radiation/grey_radiation.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_riverspread.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/production.F90               \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/lengthscaleeq.F90 $(SRCROOT)atmos_param/hs_forcing/hs_forcing.F90 $(SRCROOT)atmos_shared/tracer_driver/tropchem/tropchem_driver.F90                                            \
$(SRCROOT)shared/coupler/atmos_ocean_fluxes.F90 $(SRCROOT)shared/drifters/drifters_core.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_coriolis.F90 $(SRCROOT)atmos_param/sea_esf_rad/original_fms_rad.F90                               \
$(SRCROOT)shared/mosaic/grid.F90 $(SRCROOT)atmos_param/fsrad/hconst.F90 $(SRCROOT)atmos_param/sea_esf_rad/longwave_params.F90 $(SRCROOT)atmos_param/vert_diff_driver/vert_diff_driver.F90 $(SRCROOT)atmos_param/cosp/quickbeam/math_lib.f90                    \
$(SRCROOT)shared/time_interp/time_interp_external.F90 $(SRCROOT)atmos_fv_dynamics/model/fv_arrays.F90 $(SRCROOT)atmos_param/cloud_generator/cloud_generator.F90 $(SRCROOT)shared/amip_interp/amip_interp.F90                                                   \
$(SRCROOT)atmos_param/sea_esf_rad/esfsw_driver.F90 $(SRCROOT)atmos_param/shallow_cu/conv_closures.F90 $(SRCROOT)atmos_param/sea_esf_rad/aerosolrad_package.F90 $(SRCROOT)shared/horiz_interp/horiz_interp_spherical.F90                                        \
$(SRCROOT)atmos_fv_dynamics/driver/coupled/fv_physics.F90 $(SRCROOT)atmos_param/sea_esf_rad/longwave_clouds.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/ice_sis/mask.F90                                                                                      \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/diff_face.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_vert_kpp_mom4p0.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/ice_sis/ice_bergs.F90            \
$(SRCROOT)shared/mosaic/mosaic.F90 $(SRCROOT)atmos_param/cosp/cosp_misr_simulator.f90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_lapcst_friction.F90 $(SRCROOT)atmos_param/fsrad/fs_profile.F90                                  \
$(SRCROOT)shared/field_manager/fm_util.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_tracer_advect.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_tpm_util.F90                                              \
$(SRCROOT)atmos_shared/tracer_driver/atmos_sea_salt.F90 $(SRCROOT)shared/station_data/station_data.F90 $(SRCROOT)shared/mosaic/mosaic_util.c $(SRCROOT)atmos_param/edt/edt.F90 $(SRCROOT)atmos_param/stable_bl_turb/stable_bl_turb.F90                         \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_shortwave_csiro.F90 $(SRCROOT)atmos_param/sea_esf_rad/ozone.F90 $(SRCROOT)shared/horiz_interp/horiz_interp.F90 $(SRCROOT)atmos_param/cloud_zonal/cloud_zonal.F90                     \
$(SRCROOT)atmos_param/cosp/quickbeam/zeff.f90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_diag/ocean_tracer_util.F90 $(SRCROOT)atmos_fv_dynamics/model/tp_core.F90 $(SRCROOT)atmos_param/donner_deep/donner_rad_k.F90                                \
$(SRCROOT)shared/tracer_manager/tracer_manager.F90 $(SRCROOT)shared/fft/fft.F90 $(SRCROOT)atmos_param/cosp/quickbeam/gases.f90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_nphysicsB.F90                                          \
$(SRCROOT)atmos_shared/tracer_driver/atmos_ch3i.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/alpha_mnb.F90 $(SRCROOT)atmos_param/cosp/quickbeam/format_input.f90 $(SRCROOT)shared/astronomy/astronomy.F90               \
$(SRCROOT)atmos_fv_dynamics/tools/pmaxmin.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_vert_mix.F90 $(SRCROOT)atmos_param/shallow_cu/conv_plumes_k.F90 $(SRCROOT)atmos_param/sea_esf_rad/cloud_spec.F90                        \
$(SRCROOT)atmos_param/cloud_generator/betaDistribution.F90 $(SRCROOT)atmos_param/cosp/icarus-scops-3.7/icarus.f /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_tracer.F90 $(SRCROOT)atmos_param/ras/ras.F90                               \
$(SRCROOT)atmos_fv_dynamics/tools/set_eta.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_vert_kpp.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_vert_chen.F90                                     \
$(SRCROOT)shared/horiz_interp/horiz_interp_bilinear.F90 $(SRCROOT)shared/drifters/quicksort.F90 $(SRCROOT)atmos_shared/tracer_driver/atmos_convection_tracer.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_sbc.F90                      \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_obc.F90 $(SRCROOT)atmos_param/my25_turb/my25_turb.F90 $(SRCROOT)atmos_param/shallow_cu/conv_utilities.F90 $(SRCROOT)atmos_param/donner_deep/donner_lite_k.F90                                 \
$(SRCROOT)atmos_param/sea_esf_rad/esfsw_parameters.F90 $(SRCROOT)atmos_param/radiation_driver/radiation_driver.F90 $(SRCROOT)atmos_fv_dynamics/tools/fv_diagnostics.F90 $(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_rodas_slv.F90                         \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/turbulence.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/ice_sis/ice_grid.F90 $(SRCROOT)atmos_shared/tracer_driver/atmos_sulfate.F90                                            \
$(SRCROOT)atmos_param/sea_esf_rad/radiative_gases.F90 $(SRCROOT)atmos_param/cosp/llnl/cosp_radar.f90 $(SRCROOT)atmos_param/cosp/cosp_types.f90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_advection_velocity.F90                         \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/time.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_shortwave_jerlov.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_bgc/ocmip2_cfc.F90     \
$(SRCROOT)shared/field_manager/field_manager.F90 $(SRCROOT)atmos_shared/tracer_driver/tropchem/moz.mods.F90 $(SRCROOT)atmos_fv_dynamics/model/mapz_module.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_domains.F90                     \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_bihgen_friction.F90 $(SRCROOT)atmos_param/cosp/cosp_driver.F90 $(SRCROOT)atmos_param/sea_esf_rad/shortwave_driver.F90 $(SRCROOT)atmos_param/sea_esf_rad/lw_gases_stdtf.F90            \
$(SRCROOT)atmos_param/sea_esf_rad/microphys_cloud.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/internal_wave.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/ice_param/ice_albedo.F90                                      \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_residency_range.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_bgc/ocmip2_co2calc.F90                                                                                           \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/cmue_a.F90 $(SRCROOT)land_lad/vegetation/vegetation.F90 $(SRCROOT)atmos_fv_dynamics/model/sw_core.F90 $(SRCROOT)atmos_param/sea_esf_rad/mgrp_prscr_clds.F90                    \
$(SRCROOT)atmos_shared/tracer_driver/aer_ccn_act/aer_ccn_act.F90 $(SRCROOT)shared/time_manager/get_cal_time.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_overexchange.F90                                                     \
$(SRCROOT)shared/column_diagnostics/column_diagnostics.F90 $(SRCROOT)atmos_param/betts_miller/bm_omp.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_increment_eta.F90                                                           \
/home/wenchang/scratch/tiger3/MOM4.1/src/ocean_shared/generic_tracers/FMS_coupler_util.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_submesoscale.F90                                                                           \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_vert_const.F90 $(SRCROOT)atmos_param/sea_esf_rad/longwave_driver.F90 $(SRCROOT)shared/diag_manager/diag_axis.F90 $(SRCROOT)shared/mpp/mpp_pset.F90                                    \
/home/wenchang/scratch/tiger3/MOM4.1/src/coupler/flux_exchange.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_reduce_nocomm.h /home/wenchang/scratch/tiger3/MOM4.1/src/atmos_param/monin_obukhov/monin_obukhov_interfaces.h               \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_data_nocomm.inc /home/wenchang/scratch/tiger3/MOM4.1/src/shared/drifters/drifters_set_field.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mosaic/read_mosaic.h                             \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/fms/read_data_3d.inc /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mosaic/gradient_c2l.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_sum_sma.h                                           \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/field_manager/parse.inc /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_global_sum.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_transmit.inc                              \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_domains_define.inc /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_do_checkV.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/fms/write_data.inc                              \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/drifters/fms_switches.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_reduce_sma.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_domains_reduce.inc                        \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mosaic/constant.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mosaic/interp.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/fms/read_data_2d.inc                                                         \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/drifters/drifters_push.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_comm_nocomm.inc /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_error_a_s.h                           \
/home/wenchang/scratch/tiger3/MOM4.1/src/atmos_param/donner_deep/donner_types.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_domains_util.inc /home/wenchang/scratch/tiger3/MOM4.1/src/atmos_param/cosp/icarus-scops-3.7/congvec.inc        \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_do_update.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_io_read.inc /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_util_nocomm.inc                        \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_sum_mpi.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_reduce_mpi.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_util.inc                                \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/fms/read_data_4d.inc /home/wenchang/scratch/tiger3/MOM4.1/src/atmos_fv_dynamics/model/fv_arrays.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_io_write.inc                                 \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_get_boundary.h /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/cppdefs.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_global_field.h           \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/include/fms_platform.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_read_2Ddecomp.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mosaic/create_xgrid.h                                   \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_error_a_a.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_do_redistribute.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_write.h                          \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/drifters/drifters_compute_k.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_transmit_nocomm.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_update_domains2D.h             \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_write_2Ddecomp.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_util_sma.inc /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_chksum_scalar.h                  \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_io_util.inc /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mosaic/mosaic_util.h /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/version.h                        \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_data_sma.inc /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_global_sum_tl.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_error_s_a.h                       \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_chksum_int.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_do_updateV.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_domains_misc.inc                     \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_sum_nocomm.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_global_reduce.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_comm.inc                          \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_io_misc.inc /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_do_global_field.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_comm_sma.inc                     \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_transmit_sma.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_domains_comm.inc /home/wenchang/scratch/tiger3/MOM4.1/src/atmos_fv_dynamics/model/fv_point.inc                  \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_memory.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_error_s_s.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_chksum.h                                 \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_transmit_mpi.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_do_check.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_io_connect.inc                       \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_util_mpi.inc /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_sum.inc /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_data_mpi.inc                              \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_do_get_boundary.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_comm_mpi.inc /home/wenchang/scratch/tiger3/MOM4.1/src/atmos_param/donner_deep/donner_nml.h                   \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/system_clock.h
OBJ = physics_driver.o data_override.o random_numbers.o ocean_grids.o write_ocean_data.o lmd_ipsl_stats.o cumulus_closure_k.o ocmip2_biotic.o uw_conv.o oda_driver.o rh_clouds.o longwave.o diag_output.o cloud_interpolator.o fft99.o ocean_tpm.o             \
cosp_stats.o donner_deep_k.o donner_deep_clouds_W.o ocean_residency_ml.o ocean_bgc_restore.o sealw99.o ocean_shortwave_gfdl.o kbeq.o cloud_rad.o uw_clouds_W.o generic_tracer_utils.o atmos_tracer_utilities.o constants.o ocean_lapgen_friction.o             \
climap_albedo.o ocean_nphysics_util.o ice_dyn.o standalone_clouds.o rivers.o wet_deposition_0D.o llnl_stats.o atmos_age_tracer.o topography.o nsclock.o interp.o lidar_simulator.o sat_vapor_pres_k.o potentialml.o atmos_dust.o FMS_ocmip2_co2calc.o          \
zetac_clouds_W.o oda_types.o cosp_constants.o moistproc_kernels.o mo_chemini.o ocean_sigma_transport.o ocean_overflow.o compute_rist.o ocean_model.o donner_utilities_k.o array_lib.o oda_core.o cmue_rf.o ocean_diagnostics.o ocean_form_drag.o               \
donner_lscloud_k.o ocean_thickness.o interpolator.o coupler_types.o ocean_velocity_diag.o monin_obukhov_kernel.o mcm_sw_driver.o mpp.o atmosphere.o mo_hook.o cosp_lidar.o mpp_utilities.o shallow_physics.o mod_comm.o ocean_frazil.o fill_module.o           \
pf_to_mr.o util.o soil.o donner_cape_k.o ocean_nphysicsA.o ode_solvers.o ocean_bihcst_friction.o moz.subs.o mpp_parameter.o MISR_simulator.o axis_utils.o isccp_clouds.o ocean_rough.o init_dry_atm.o load_hydrometeor_classes.o mpp_io.o vert_turb_driver.o   \
adv_center.o dry_adj.o gmean.o tracer_2d.o co2int.o bulkphys_rad.o strat_clouds_W.o shr_kind_mod.o timingModule.o diag_cloud_rad.o ocean_util.o topo_drag.o horiz_interp_conserve.o cu_mo_trans.o lin_cloud_microphys.o ocean_xlandinsert.o mo_chemdr.o        \
ocean_rivermix.o monin_obukhov.o mg_drag.o drifters_comm.o shortwave.o ocean_albedo.o load_mie_table.o ocean_velocity.o atmos_lib.o ocean_increment_velocity.o generic_BLING.o mo_imp_slv.o mcm_swtbls.o ocean_sponges_eta.o ocean_residency_meta.o clouds.o   \
read_mosaic.o fms_io.o mcm_swnew.o upper.o optical_path.o ocean_types.o ocean_residency.o radar_simulator_types.o aer_ccn_act_k.o pv_module.o gridinterpol.o scops.o lagrange.o time_interp.o longwave_tables.o ocean_nphysicsC.o specified_clouds_W.o         \
atmos_co2.o coupler_main.o ocean_momentum_source.o gaussian_topog.o memutils.o cmue_ma.o generic_CFC.o nonfms_donner.o cmue_b.o atmos_carbon_aerosol.o getmax.o fms.o cosp_io.o cloudrad_diagnostics.o fms_donner.o atmos_nudge.o ocean_po4_pre.o ocean_bbc.o  \
diag_manager.o conv_utilities_k.o variances.o ocean_pert_co2.o ocean_age_tracer.o tridiagonal.o diag_cloud.o drifters_io.o ocean_barotropic.o land_types.o ocean_tracer_diag.o mpp_domains.o diag_grid.o atmos_model.o ocean_generic_tracer.o xgrid.o          \
ispralength.o ocean_density.o transport_matrix.o ocean_xlandmix.o diag_data.o microphys_rad.o tridiagonal_gotm.o rot.o atmos_soa.o ocean_lap_friction.o diffusivity.o mcm_lw.o ice_model.o gradient_c2l.o strat_cloud.o land_model.o vert_diff.o               \
ocean_sponges_velocity.o mo_photo.o ocean_bih_tracer.o fk_craig.o radar_simulator.o q2over2eq.o eqstate.o generic_tracer.o ocean_vert_pp.o moz.mat.o mo_usrrxt.o conv_plumes.o gotm_lib_version.o ice_spec.o update_fv_phys.o ocean_adv_vel_diag.o platform.o  \
horiz_interp_type.o cmue_sg.o strat_chem_model.o moist_processes_utils.o ocean_increment_tracer.o ocean_time_filter.o rh_based_clouds.o init_sw_ic.o horiz_interp_bicubic.o surface_flux.o radiation_diag.o atmos_sulfur_hex.o bm_massflux.o algebraiclength.o \
dyn_core.o fsrad.o ocean_tempsalt.o drifters.o ocmip2_he.o age_of_air.o vert_advection.o memuse.o deep_conv.o fv_pack.o cloud_obs.o mrgrnk.o ocean_bih_friction.o shallow_conv.o fv_dynamics.o lscale_cond.o xbt_drop_rate_adjust.o mo_setinv.o                \
atmos_tracer_driver.o threadloc.o donner_cloud_model_k.o cloudrad_package.o dissipationeq.o tkeeq.o ocean_workspace.o ocean_lap_tracer.o ensemble_manager.o ocean_topog.o gradient.o ocean_polar_filter.o cg_drag.o prec_scops.o co2_data.o donner_types.o     \
drifters_input.o ocean_pressure.o mpp_memutils.o ocean_operators.o moist_processes.o entrain.o ocean_drifters.o ocean_mixdownslope.o ocean_vert_gotm.o tkealgebraic.o ice_thm.o par_vecsum.o cmue_c.o atmos_radon.o genericeq.o diff_center.o r_ratio.o        \
sat_vapor_pres.o mo_read_sim_chm.o mo_chem_utls.o aerosol.o strat_chem_utilities.o damping_driver.o ocean_convect.o cosp_isccp_simulator.o donner_deep.o time_manager.o stock_constants.o sea_esf_rad.o rad_utilities.o diag_integral.o ocean_parameters.o     \
isccp_cloud_types.o longwave_fluxes.o ocean_nphysics.o numerics.o pft_module.o kpp.o betts_miller.o ocean_vert_tidal.o generic_TOPAZ.o mo_setsox.o cmue_d.o mo_exp_slv.o mo_jpl.o m_tracname.o diag_util.o fv_restart.o diag_clouds_W.o compute_cpsi3.o        \
MersenneTwister.o donner_deep_miz.o ocean_velocity_advect.o land_properties.o rdparm.o gas_tf.o lhsw_driver.o strat_chem_driver.o ice_type.o rad_diag.o ocean_ibgc.o create_xgrid.o epsbalgebraic.o mpp_data.o optics_lib.o ocean_passive.o                    \
ocean_residency_integrand.o aer_in_act.o rad_output_file.o ecmfft.o cosp_utils.o ocean_shortwave.o ocean_sponges_tracer.o donner_meso_k.o kbalgebraic.o moist_conv.o dsd.o ocmip2_abiotic.o cosp_simulator.o convert_fluxes.o cosp.o grey_radiation.o          \
ocean_riverspread.o production.o lengthscaleeq.o hs_forcing.o tropchem_driver.o atmos_ocean_fluxes.o drifters_core.o ocean_coriolis.o original_fms_rad.o grid.o hconst.o longwave_params.o vert_diff_driver.o math_lib.o time_interp_external.o fv_arrays.o    \
cloud_generator.o amip_interp.o esfsw_driver.o conv_closures.o aerosolrad_package.o horiz_interp_spherical.o fv_physics.o longwave_clouds.o mask.o diff_face.o ocean_vert_kpp_mom4p0.o ice_bergs.o mosaic.o cosp_misr_simulator.o ocean_lapcst_friction.o      \
fs_profile.o fm_util.o ocean_tracer_advect.o ocean_tpm_util.o atmos_sea_salt.o station_data.o mosaic_util.o edt.o stable_bl_turb.o ocean_shortwave_csiro.o ozone.o horiz_interp.o cloud_zonal.o zeff.o ocean_tracer_util.o tp_core.o donner_rad_k.o            \
tracer_manager.o fft.o gases.o ocean_nphysicsB.o atmos_ch3i.o alpha_mnb.o format_input.o astronomy.o pmaxmin.o ocean_vert_mix.o conv_plumes_k.o cloud_spec.o betaDistribution.o icarus.o ocean_tracer.o ras.o set_eta.o ocean_vert_kpp.o ocean_vert_chen.o     \
horiz_interp_bilinear.o quicksort.o atmos_convection_tracer.o ocean_sbc.o ocean_obc.o my25_turb.o conv_utilities.o donner_lite_k.o esfsw_parameters.o radiation_driver.o fv_diagnostics.o mo_rodas_slv.o turbulence.o ice_grid.o atmos_sulfate.o               \
radiative_gases.o cosp_radar.o cosp_types.o ocean_advection_velocity.o time.o ocean_shortwave_jerlov.o ocmip2_cfc.o field_manager.o moz.mods.o mapz_module.o ocean_domains.o ocean_bihgen_friction.o cosp_driver.o shortwave_driver.o lw_gases_stdtf.o         \
microphys_cloud.o internal_wave.o ice_albedo.o ocean_residency_range.o ocmip2_co2calc.o cmue_a.o vegetation.o sw_core.o mgrp_prscr_clds.o aer_ccn_act.o get_cal_time.o ocean_overexchange.o column_diagnostics.o bm_omp.o ocean_increment_eta.o                \
FMS_coupler_util.o ocean_submesoscale.o ocean_vert_const.o longwave_driver.o diag_axis.o mpp_pset.o flux_exchange.o
OFF = /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_write.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_error_a_a.h $(SRCROOT)shared/amip_interp/amip_interp.F90 $(SRCROOT)shared/oda_tools/xbt_drop_rate_adjust.f90     \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_velocity_advect.F90 $(SRCROOT)atmos_param/cosp/icarus-scops-3.7/icarus.f $(SRCROOT)shared/diag_manager/diag_manager.F90 $(SRCROOT)shared/platform/platform.F90                                \
$(SRCROOT)atmos_shared/tracer_driver/atmos_radon.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/genericeq.F90 $(SRCROOT)atmos_param/donner_deep/fms_donner.F90                                                            \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/lagrange.F90 $(SRCROOT)atmos_param/sea_esf_rad/specified_clouds_W.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_advection_velocity.F90                        \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_io_misc.inc $(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_photo.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_sigma_transport.F90                            \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_comm.inc $(SRCROOT)atmos_fv_dynamics/tools/timingModule.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_bgc/ocmip2_abiotic.F90                                                       \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_global_reduce.h /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_model.F90 $(SRCROOT)atmos_shared/tracer_driver/atmos_sulfur_hex.F90                                           \
$(SRCROOT)atmos_param/shallow_cu/conv_utilities.F90 $(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_imp_slv.F90 $(SRCROOT)atmos_param/strat_cloud/strat_cloud.F90 $(SRCROOT)atmos_param/sea_esf_rad/strat_clouds_W.F90                                        \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_workspace.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/epsbalgebraic.F90                                                                               \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_xlandmix.F90 $(SRCROOT)shared/random_numbers/MersenneTwister.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_chksum.h                                            \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_lap_tracer.F90 $(SRCROOT)shared/mosaic/interp.c $(SRCROOT)atmos_param/cloud_obs/cloud_obs.F90 $(SRCROOT)shared/tridiagonal/tridiagonal.F90                                            \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/system_clock.h $(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_chemdr.F90 $(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_chemini.F90 $(SRCROOT)atmos_param/sea_esf_rad/longwave_fluxes.F90      \
$(SRCROOT)atmos_param/sea_esf_rad/uw_clouds_W.F90 $(SRCROOT)atmos_shared/tracer_driver/atmos_ch3i.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/turbulence.F90                                                           \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_bihcst_friction.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/atmos_param/monin_obukhov/monin_obukhov_interfaces.h $(SRCROOT)shared/oda_tools/write_ocean_data.F90                     \
$(SRCROOT)atmos_param/cosp/quickbeam/dsd.f90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/diff_face.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/coupler/flux_exchange.F90                                                        \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_sponges_velocity.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/dissipationeq.F90 $(SRCROOT)atmos_param/donner_deep/donner_deep.F90             \
$(SRCROOT)atmos_param/sea_esf_rad/standalone_clouds.F90 $(SRCROOT)atmos_shared/tracer_driver/atmos_soa.F90 $(SRCROOT)shared/diag_manager/diag_axis.F90 $(SRCROOT)shared/sat_vapor_pres/sat_vapor_pres.F90 $(SRCROOT)atmos_param/cosp/quickbeam/gases.f90       \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/field_manager/parse.inc $(SRCROOT)shared/horiz_interp/horiz_interp_bicubic.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/compute_rist.F90                                \
$(SRCROOT)atmos_fv_dynamics/tools/init_dry_atm.F90 $(SRCROOT)atmos_param/cosp/quickbeam/format_input.f90 $(SRCROOT)land_lad/land_model.F90 $(SRCROOT)shared/memutils/memutils.F90                                                                              \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_shortwave_jerlov.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_momentum_source.F90                                                                   \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_error_a_s.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/drifters/drifters_push.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/fms/read_data_2d.inc                                      \
$(SRCROOT)atmos_fv_dynamics/model/sw_core.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_domains_util.inc $(SRCROOT)atmos_param/sea_esf_rad/longwave_params.F90                                                                           \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_lapgen_friction.F90 $(SRCROOT)atmos_param/sea_esf_rad/aerosolrad_package.F90 $(SRCROOT)atmos_param/shallow_cu/deep_conv.F90 $(SRCROOT)atmos_fv_dynamics/tools/init_sw_ic.F90          \
$(SRCROOT)land_lad/soil/soil.F90 $(SRCROOT)shared/fms/fms.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/ice_sis/ice_dyn.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mosaic/create_xgrid.h                                                               \
$(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_read_sim_chm.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_vert_gotm.F90 $(SRCROOT)atmos_param/donner_deep/donner_types.F90 $(SRCROOT)shared/mpp/mpp_io.F90                    \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_nphysicsC.F90 $(SRCROOT)atmos_param/donner_deep/donner_meso_k.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/drifters/drifters_compute_k.h                                       \
$(SRCROOT)atmos_shared/tracer_driver/atmos_sea_salt.F90 $(SRCROOT)atmos_param/fsrad/co2int.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_error_s_a.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_chksum_scalar.h     \
$(SRCROOT)shared/mosaic/read_mosaic.c $(SRCROOT)atmos_shared/tracer_driver/tropchem/tropchem_driver.F90 $(SRCROOT)shared/coupler/atmos_ocean_fluxes.F90 $(SRCROOT)atmos_param/sea_esf_rad/bulkphys_rad.F90                                                     \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_pressure.F90 $(SRCROOT)atmos_param/betts_miller/bm_omp.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_diag/ocean_drifters.F90 $(SRCROOT)atmos_param/cosp/quickbeam/mrgrnk.f90      \
$(SRCROOT)atmos_param/sea_esf_rad/esfsw_driver.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_diag/ocean_diagnostics.F90 $(SRCROOT)atmos_param/cosp/quickbeam/zeff.f90 $(SRCROOT)atmos_shared/tracer_driver/aer_ccn_act/aer_ccn_act_k.F90           \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_io_connect.inc $(SRCROOT)atmos_param/fsrad/hconst.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_transmit_mpi.h $(SRCROOT)atmos_param/clouds/clouds.F90                   \
$(SRCROOT)atmos_param/sea_esf_rad/cloud_spec.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/ode_solvers.F90 $(SRCROOT)atmos_shared/interpolator/interpolator.F90 $(SRCROOT)atmos_param/monin_obukhov/monin_obukhov.F90          \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mosaic/read_mosaic.h $(SRCROOT)atmos_param/sea_esf_rad/shortwave_driver.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_shortwave_gfdl.F90                                       \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/kbeq.F90 $(SRCROOT)atmos_param/cosp/quickbeam/load_mie_table.f90 $(SRCROOT)atmos_param/diffusivity/diffusivity.F90                                                             \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_passive.F90 $(SRCROOT)shared/mpp/mpp_pset.F90 $(SRCROOT)shared/mpp/mpp.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_global_sum.h                                    \
$(SRCROOT)atmos_param/sea_esf_rad/microphys_rad.F90 $(SRCROOT)atmos_param/fsrad/longwave.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_sum_sma.h $(SRCROOT)land_lad/soil/land_properties.F90 $(SRCROOT)atmos_param/edt/edt.F90           \
$(SRCROOT)atmos_fv_dynamics/tools/age_of_air.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/variances.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/drifters/fms_switches.h                                         \
$(SRCROOT)atmos_param/cloud_generator/betaDistribution.F90 $(SRCROOT)shared/drifters/drifters_input.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mosaic/interp.h                                                                                        \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_nphysics_util.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/atmos_param/donner_deep/donner_types.h $(SRCROOT)atmos_fv_dynamics/model/fv_pack.F90                                       \
$(SRCROOT)shared/astronomy/astronomy.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_xlandinsert.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_coriolis.F90                                               \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/fms/read_data_4d.inc $(SRCROOT)atmos_param/sea_esf_rad/cloudrad_diagnostics.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/eqstate.F90                                          \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_global_field.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_get_boundary.h /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_bgc/ocmip2_he.F90                          \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/tkeeq.F90 $(SRCROOT)atmos_fv_dynamics/tools/set_eta.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/cmue_c.F90                             \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_residency.F90 $(SRCROOT)shared/mpp/nsclock.c $(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_hook.F90 $(SRCROOT)atmos_param/cosp/actsim/lidar_simulator.f90                               \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_bgc/ocmip2_co2calc.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_util_sma.inc $(SRCROOT)atmos_param/monin_obukhov/monin_obukhov_kernel.F90                                         \
$(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_chem_utls.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_data_sma.inc /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_vert_const.F90                            \
$(SRCROOT)atmos_param/sea_esf_rad/sealw99.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_domains.F90 $(SRCROOT)atmos_param/donner_deep/donner_deep_miz.F90 $(SRCROOT)atmos_shared/tracer_driver/atmos_age_tracer.F90                     \
$(SRCROOT)shared/diag_manager/diag_data.F90 $(SRCROOT)shared/horiz_interp/horiz_interp_conserve.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_topog.F90 $(SRCROOT)atmos_param/diag_cloud/diag_cloud.F90                                 \
$(SRCROOT)atmos_fv_dynamics/model/fv_dynamics.F90 $(SRCROOT)atmos_param/mg_drag/mg_drag.F90 $(SRCROOT)atmos_shared/tracer_driver/stratchem/strat_chem_driver.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/ice_sis/rot.F90                                      \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_mixdownslope.F90 $(SRCROOT)shared/fms/fms_io.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_reduce_nocomm.h $(SRCROOT)shared/time_manager/get_cal_time.F90       \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_vert_kpp_mom4p0.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/algebraiclength.F90 $(SRCROOT)shared/axis_utils/axis_utils.F90                    \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_form_drag.F90 $(SRCROOT)atmos_param/cosp/cosp.f90 $(SRCROOT)shared/data_override/data_override.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_tpm_util.F90   \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/q2over2eq.F90 $(SRCROOT)atmos_param/cosp/cosp_constants.f90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_sbc.F90                                           \
$(SRCROOT)shared/drifters/cloud_interpolator.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/cmue_rf.F90 $(SRCROOT)atmos_shared/tracer_driver/atmos_tracer_driver.F90                                                      \
/home/wenchang/scratch/tiger3/MOM4.1/src/ice_sis/ice_model.F90 $(SRCROOT)atmos_param/donner_deep/donner_utilities_k.F90 $(SRCROOT)atmos_fv_dynamics/tools/mod_comm.F90 $(SRCROOT)atmos_param/cosp/llnl/llnl_stats.f90                                          \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/cppdefs.h /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_overflow.F90 $(SRCROOT)atmos_param/donner_deep/wet_deposition_0D.F90                          \
$(SRCROOT)atmos_param/sea_esf_rad/radiation_diag.F90 $(SRCROOT)atmos_shared/tracer_driver/atmos_convection_tracer.F90 $(SRCROOT)atmos_param/cloud_rad/cloud_rad.F90 $(SRCROOT)atmos_param/cosp/cosp_simulator.f90                                              \
/home/wenchang/scratch/tiger3/MOM4.1/src/coupler/coupler_main.F90 $(SRCROOT)atmos_param/sea_esf_rad/sea_esf_rad.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_transmit_nocomm.h                                                          \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_shortwave_csiro.F90 $(SRCROOT)shared/mosaic/mosaic.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_vert_mix.F90                                         \
$(SRCROOT)shared/drifters/drifters_comm.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_chksum_int.h /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_polar_filter.F90                                            \
$(SRCROOT)atmos_param/donner_deep/donner_lite_k.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/include/version.h $(SRCROOT)land_param/climap_albedo.F90 $(SRCROOT)atmos_param/sea_esf_rad/diag_clouds_W.F90                          \
$(SRCROOT)atmos_param/fsrad/mcm_swnew.F90 $(SRCROOT)shared/time_interp/time_interp.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/kbalgebraic.F90 $(SRCROOT)atmos_fv_dynamics/model/pft_module.F90                        \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_vert_pp.F90 $(SRCROOT)atmos_param/cosp/cosp_driver.F90 $(SRCROOT)atmos_param/cosp/cosp_types.f90                                                                                      \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_tracer_advect.F90 $(SRCROOT)atmos_shared/tracer_driver/tropchem/moz.mat.F90 $(SRCROOT)land_lad/soil/rivers.F90 $(SRCROOT)atmos_param/moist_processes/moist_processes_utils.F90             \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_do_check.h /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_diag/ocean_tracer_diag.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_comm_mpi.inc                       \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_thickness.F90 $(SRCROOT)atmos_param/sea_esf_rad/donner_deep_clouds_W.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/transport_matrix.F90                                   \
$(SRCROOT)atmos_shared/tracer_driver/atmos_co2.F90 $(SRCROOT)shared/oda_tools/oda_types.F90 $(SRCROOT)atmos_param/moist_processes/moist_processes.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/ocean_shared/generic_tracers/FMS_coupler_util.F90               \
$(SRCROOT)atmos_param/fsrad/mcm_lw.F90 $(SRCROOT)atmos_fv_dynamics/tools/getmax.F90 $(SRCROOT)atmos_fv_dynamics/model/update_fv_phys.F90 $(SRCROOT)atmos_param/donner_deep/donner_deep_k.F90 $(SRCROOT)atmos_param/cosp/cosp_lidar.f90                         \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_age_tracer.F90 $(SRCROOT)shared/drifters/drifters.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_sponges_eta.F90                                            \
$(SRCROOT)atmos_param/cosp/icarus-scops-3.7/scops.f /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_residency_ml.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/ice_param/ice_albedo.F90                                                     \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/cmue_d.F90 $(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_setinv.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/alpha_mnb.F90           \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_parameters.F90 $(SRCROOT)atmos_param/sea_esf_rad/longwave_tables.F90 $(SRCROOT)atmos_param/ras/ras.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_diag/ocean_adv_vel_diag.F90      \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_tempsalt.F90 $(SRCROOT)atmos_fv_dynamics/tools/gmean.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/kpp.F90                                           \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_bgc/ocean_pert_co2.F90 $(SRCROOT)atmos_param/shallow_cu/conv_plumes.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_obc.F90                                                         \
$(SRCROOT)atmos_shared/tracer_driver/tropchem/moz.mods.F90 $(SRCROOT)atmos_param/shallow_cu/uw_conv.F90 $(SRCROOT)atmos_param/physics_driver/physics_driver.F90 $(SRCROOT)shared/mosaic/grid.F90 $(SRCROOT)atmos_shared/vert_advection/vert_advection.F90      \
$(SRCROOT)atmos_param/sea_esf_rad/cloudrad_package.F90 $(SRCROOT)atmos_param/betts_miller/betts_miller.F90 $(SRCROOT)atmos_param/fsrad/rad_diag.F90 $(SRCROOT)atmos_param/cosp/quickbeam/math_lib.f90 $(SRCROOT)shared/tracer_manager/tracer_manager.F90       \
$(SRCROOT)atmos_param/sea_esf_rad/rad_utilities.F90 $(SRCROOT)shared/mosaic/gradient.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_diag/ocean_tracer_util.F90 $(SRCROOT)atmos_param/sea_esf_rad/esfsw_parameters.F90                               \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_util_nocomm.inc /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/diff_center.F90 $(SRCROOT)atmos_fv_dynamics/driver/coupled/atmosphere.F90                            \
$(SRCROOT)shared/horiz_interp/horiz_interp_spherical.F90 $(SRCROOT)atmos_fv_dynamics/model/ecmfft.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_do_redistribute.h $(SRCROOT)atmos_fv_dynamics/model/dyn_core.F90                         \
$(SRCROOT)atmos_param/cosp/quickbeam/atmos_lib.f90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_velocity.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_bih_tracer.F90                                       \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_increment_tracer.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_barotropic.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_global_sum_tl.h \
$(SRCROOT)shared/fft/fft99.F90 $(SRCROOT)atmos_param/shallow_cu/conv_closures.F90 $(SRCROOT)atmos_fv_dynamics/model/shr_kind_mod.F90 $(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_setsox.F90                                                               \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_memory.h /home/wenchang/scratch/tiger3/MOM4.1/src/atmos_fv_dynamics/model/fv_point.inc /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/ispralength.F90        \
$(SRCROOT)atmos_param/cosp/quickbeam/radar_simulator.f90 $(SRCROOT)atmos_param/cloud_generator/cloud_generator.F90 $(SRCROOT)atmos_fv_dynamics/model/fv_arrays.F90 $(SRCROOT)atmos_param/lscale_cond/lscale_cond.F90                                           \
$(SRCROOT)atmos_fv_dynamics/driver/coupled/fv_physics.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/coupler/surface_flux.F90 $(SRCROOT)atmos_shared/tracer_driver/atmos_carbon_aerosol.F90                                                                      \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_operators.F90 $(SRCROOT)atmos_param/shallow_cu/conv_utilities_k.F90 $(SRCROOT)atmos_param/grey_radiation/grey_radiation.F90 $(SRCROOT)atmos_param/donner_deep/donner_rad_k.F90                \
$(SRCROOT)atmos_param/cosp/actsim/lmd_ipsl_stats.f90 $(SRCROOT)shared/mpp/mpp_data.F90 $(SRCROOT)atmos_param/cosp/quickbeam/load_hydrometeor_classes.f90 $(SRCROOT)atmos_param/vert_diff/vert_diff.F90                                                         \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_bgc/ocmip2_cfc.F90 $(SRCROOT)atmos_shared/atmos_nudge/atmos_nudge.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/gridinterpol.F90                                         \
$(SRCROOT)shared/diag_manager/diag_output.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_data_nocomm.inc /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_do_checkV.h $(SRCROOT)atmos_fv_dynamics/model/fill_module.F90    \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_riverspread.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_diag/ocean_velocity_diag.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mosaic/constant.h                 \
$(SRCROOT)atmos_param/cosp/cosp_isccp_simulator.f90 $(SRCROOT)atmos_param/entrain/entrain.F90 $(SRCROOT)atmos_param/sea_esf_rad/rad_output_file.F90 $(SRCROOT)atmos_param/fsrad/fs_profile.F90 $(SRCROOT)atmos_param/donner_deep/donner_cloud_model_k.F90      \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_lap_friction.F90 $(SRCROOT)shared/fft/fft.F90 $(SRCROOT)atmos_param/cloud_zonal/cloud_zonal.F90 $(SRCROOT)shared/horiz_interp/horiz_interp_type.F90                                   \
$(SRCROOT)shared/mpp/mpp_parameter.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_lapcst_friction.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_frazil.F90                                             \
$(SRCROOT)atmos_param/sea_esf_rad/aerosol.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_density.F90 $(SRCROOT)atmos_fv_dynamics/tools/par_vecsum.F90 $(SRCROOT)atmos_param/sea_esf_rad/radiative_gases.F90                              \
$(SRCROOT)atmos_shared/tracer_driver/tropchem/moz.subs.F90 $(SRCROOT)atmos_param/hs_forcing/hs_forcing.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/ocean_shared/generic_tracers/generic_tracer.F90 $(SRCROOT)shared/horiz_interp/horiz_interp_bilinear.F90    \
$(SRCROOT)shared/random_numbers/random_numbers.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_read_2Ddecomp.h $(SRCROOT)shared/time_manager/time_manager.F90 $(SRCROOT)shared/coupler/coupler_types.F90                                   \
$(SRCROOT)shared/exchange/stock_constants.F90 $(SRCROOT)shared/topography/gaussian_topog.F90 $(SRCROOT)land_lad/vegetation/vegetation.F90 $(SRCROOT)atmos_fv_dynamics/tools/fv_diagnostics.F90                                                                 \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mosaic/mosaic_util.h /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/production.F90 $(SRCROOT)atmos_param/donner_deep/cumulus_closure_k.F90                                    \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/adv_center.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/cmue_sg.F90 $(SRCROOT)shared/drifters/drifters_core.F90                               \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_domains_comm.inc $(SRCROOT)land_lad/land_types.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/compute_cpsi3.F90                                           \
$(SRCROOT)atmos_param/cosp/icarus-scops-3.7/isccp_cloud_types.f $(SRCROOT)atmos_param/cosp/cosp_io.f90 $(SRCROOT)shared/mosaic/mosaic_util.c /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/cmue_b.F90                        \
$(SRCROOT)atmos_param/fsrad/rdparm.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/ocean_shared/generic_tracers/generic_BLING.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_sponges_tracer.F90                                    \
$(SRCROOT)atmos_param/sea_esf_rad/rh_based_clouds.F90 $(SRCROOT)atmos_param/cosp/cosp_stats.f90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_vert_kpp.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/ice_sis/mask.F90                \
$(SRCROOT)atmos_fv_dynamics/tools/pmaxmin.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/atmos_param/donner_deep/donner_nml.h $(SRCROOT)shared/constants/constants.F90 $(SRCROOT)atmos_param/sea_esf_rad/longwave_driver.F90                                     \
$(SRCROOT)atmos_param/dry_adj/dry_adj.F90 $(SRCROOT)shared/topography/topography.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_data_mpi.inc $(SRCROOT)atmos_param/radiation_driver/radiation_driver.F90                                  \
$(SRCROOT)atmos_fv_dynamics/model/mapz_module.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_bgc/ocean_bgc_restore.F90 $(SRCROOT)shared/drifters/quicksort.F90 $(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_usrrxt.F90                          \
$(SRCROOT)atmos_param/rh_clouds/rh_clouds.F90 $(SRCROOT)atmos_param/sea_esf_rad/gas_tf.F90 $(SRCROOT)atmos_param/cosp/llnl/cosp_radar.f90 $(SRCROOT)atmos_param/cosp/llnl/pf_to_mr.f                                                                           \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_convect.F90 $(SRCROOT)atmos_shared/tracer_driver/tropchem/strat_chem_utilities.F90 $(SRCROOT)atmos_param/cosp/quickbeam/array_lib.f90                                                 \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_domains_reduce.inc $(SRCROOT)atmos_param/shallow_cu/conv_plumes_k.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/tridiagonal_gotm.F90                           \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/fms/write_data.inc $(SRCROOT)atmos_param/moist_processes/moistproc_kernels.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_nphysicsA.F90                                          \
/home/wenchang/scratch/tiger3/MOM4.1/src/ice_param/ocean_rough.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_do_update.h /home/wenchang/scratch/tiger3/MOM4.1/src/atmos_param/cosp/icarus-scops-3.7/congvec.inc                          \
$(SRCROOT)atmos_param/sea_esf_rad/lw_gases_stdtf.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_submesoscale.F90 $(SRCROOT)land_lad/numerics.F90 $(SRCROOT)atmos_param/fsrad/mcm_sw_driver.F90                                   \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_reduce_mpi.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_sum_mpi.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_io_read.inc                             \
$(SRCROOT)atmos_param/diag_cloud_rad/diag_cloud_rad.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_bgc/ocmip2_biotic.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_tracer.F90                                             \
$(SRCROOT)atmos_param/cosp/MISR_simulator/MISR_simulator.f $(SRCROOT)atmos_shared/tracer_driver/tropchem/m_tracname.F90 $(SRCROOT)atmos_param/vert_turb_driver/vert_turb_driver.F90 $(SRCROOT)atmos_param/betts_miller/bm_massflux.F90                         \
$(SRCROOT)shared/horiz_interp/horiz_interp.F90 $(SRCROOT)shared/mosaic/create_xgrid.c /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_do_updateV.h $(SRCROOT)atmos_shared/tracer_driver/atmos_tracer_utilities.F90                             \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_io_util.inc /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_nphysicsB.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_residency_range.F90     \
$(SRCROOT)atmos_param/lin_cloud_microphys/lin_cloud_microphys.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/ice_sis/ice_spec.F90 $(SRCROOT)shared/field_manager/field_manager.F90 $(SRCROOT)atmos_param/cu_mo_trans/cu_mo_trans.F90                             \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_sum_nocomm.h $(SRCROOT)shared/field_manager/fm_util.F90 $(SRCROOT)atmos_param/sea_esf_rad/mgrp_prscr_clds.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_transmit_sma.h   \
$(SRCROOT)atmos_param/moist_conv/moist_conv.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_do_global_field.h $(SRCROOT)atmos_fv_dynamics/tools/pv_module.F90 $(SRCROOT)shared/column_diagnostics/column_diagnostics.F90                   \
/home/wenchang/scratch/tiger3/MOM4.1/src/ocean_shared/generic_tracers/generic_CFC.F90 $(SRCROOT)atmos_param/sea_esf_rad/optical_path.F90 $(SRCROOT)atmos_param/donner_deep/donner_cape_k.F90 $(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_rodas_slv.F90    \
$(SRCROOT)shared/diag_manager/diag_util.F90 $(SRCROOT)atmos_param/cg_drag/cg_drag.F90 $(SRCROOT)shared/memutils/memuse.c $(SRCROOT)atmos_param/fsrad/co2_data.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/time.F90           \
$(SRCROOT)atmos_param/cosp/quickbeam/optics_lib.f90 $(SRCROOT)atmos_param/topo_drag/topo_drag.F90 $(SRCROOT)shared/mosaic/gradient_c2l.c /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_util_mpi.inc                                          \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_vert_chen.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/util.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/ice_param/ocean_albedo.F90                  \
$(SRCROOT)atmos_param/damping_driver/damping_driver.F90 $(SRCROOT)atmos_shared/tracer_driver/stratchem/strat_chem_model.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_rivermix.F90                                             \
$(SRCROOT)atmos_param/diag_integral/diag_integral.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_sum.inc $(SRCROOT)shared/sat_vapor_pres/sat_vapor_pres_k.F90                                                                             \
/home/wenchang/scratch/tiger3/MOM4.1/src/ocean_shared/generic_tracers/generic_tracer_utils.F90 $(SRCROOT)atmos_param/sea_esf_rad/original_fms_rad.F90 $(SRCROOT)atmos_param/cosp/llnl/prec_scops.f                                                             \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mosaic/gradient_c2l.h /home/wenchang/scratch/tiger3/MOM4.1/src/shared/drifters/drifters_set_field.h /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_vert_tidal.F90                    \
$(SRCROOT)shared/drifters/drifters_io.F90 $(SRCROOT)shared/mpp/mpp_memutils.F90 $(SRCROOT)atmos_param/stable_bl_turb/stable_bl_turb.F90 $(SRCROOT)atmos_param/donner_deep/donner_lscloud_k.F90 $(SRCROOT)atmos_fv_dynamics/tools/upper.F90                     \
/home/wenchang/scratch/tiger3/MOM4.1/src/ocean_shared/generic_tracers/FMS_ocmip2_co2calc.F90 $(SRCROOT)atmos_param/donner_deep/nonfms_donner.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/util/convert_fluxes.F90                  \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_comm_nocomm.inc $(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_jpl.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_overexchange.F90                            \
/home/wenchang/scratch/tiger3/MOM4.1/src/ice_sis/ice_bergs.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_tpm.F90 $(SRCROOT)atmos_shared/tracer_driver/tropchem/mo_exp_slv.F90 $(SRCROOT)shared/coupler/ensemble_manager.F90          \
/home/wenchang/scratch/tiger3/MOM4.1/src/atmos_fv_dynamics/model/fv_arrays.h $(SRCROOT)atmos_param/sea_esf_rad/ozone.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_util.inc $(SRCROOT)atmos_fv_dynamics/tools/fv_restart.F90             \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_nphysics.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/include/fms_platform.h $(SRCROOT)atmos_shared/tracer_driver/aer_ccn_act/aer_in_act.F90                                   \
$(SRCROOT)atmos_shared/tracer_driver/aer_ccn_act/aer_ccn_act.F90 $(SRCROOT)atmos_param/cosp/quickbeam/radar_simulator_types.f90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_io_write.inc $(SRCROOT)atmos_param/fsrad/mcm_swtbls.F90        \
$(SRCROOT)atmos_param/shallow_conv/shallow_conv.F90 $(SRCROOT)atmos_param/sea_esf_rad/longwave_clouds.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/lengthscaleeq.F90                                                    \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/fk_craig.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_update_domains2D.h                                                                                \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_write_2Ddecomp.h /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_increment_eta.F90                                                                                   \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/gotm_lib_version.F90 $(SRCROOT)shared/mpp/threadloc.c $(SRCROOT)atmos_param/sea_esf_rad/zetac_clouds_W.F90                                                                     \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_grids.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/ocean_shared/generic_tracers/generic_TOPAZ.F90                                                                                             \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_increment_velocity.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_shortwave.F90                                                                       \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_bgc/ocean_po4_pre.F90 $(SRCROOT)atmos_param/sea_esf_rad/isccp_clouds.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/r_ratio.F90                                     \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_bgc/ocean_ibgc.F90 $(SRCROOT)atmos_param/sea_esf_rad/microphys_cloud.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_domains_misc.inc $(SRCROOT)shared/mpp/mpp_utilities.F90         \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_bbc.F90 $(SRCROOT)atmos_param/cosp/cosp_utils.f90 $(SRCROOT)shared/mpp/mpp_domains.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_comm_sma.inc                           \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_util.F90 $(SRCROOT)atmos_param/my25_turb/my25_turb.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/tkealgebraic.F90 $(SRCROOT)atmos_param/fsrad/fsrad.F90 \
/home/wenchang/scratch/tiger3/MOM4.1/src/ice_sis/ice_grid.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_error_s_s.h $(SRCROOT)atmos_shared/tracer_driver/atmos_dust.F90 $(SRCROOT)atmos_shared/tracer_driver/atmos_sulfate.F90           \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/sources/ocean_time_filter.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_do_get_boundary.h $(SRCROOT)atmos_fv_dynamics/model/tracer_2d.F90                                    \
$(SRCROOT)atmos_param/shallow_physics/shallow_physics.F90 $(SRCROOT)atmos_param/vert_diff_driver/vert_diff_driver.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/fms/read_data_3d.inc /home/wenchang/scratch/tiger3/MOM4.1/src/ice_sis/ice_type.F90       \
$(SRCROOT)shared/diag_manager/diag_grid.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/ocean_types.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_domains_define.inc                                                      \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_bih_friction.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/cmue_ma.F90                                                                          \
/home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_transmit.inc $(SRCROOT)shared/station_data/station_data.F90 $(SRCROOT)atmos_param/cosp/cosp_misr_simulator.f90 $(SRCROOT)atmos_coupled/atmos_model.F90                                         \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_core/oda_driver.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_residency_meta.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/shared/mpp/include/mpp_reduce_sma.h                  \
$(SRCROOT)shared/oda_tools/oda_core.F90 $(SRCROOT)shared/time_interp/time_interp_external.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_tracers/ocean_residency_integrand.F90 $(SRCROOT)atmos_param/fsrad/shortwave.F90                            \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_bgc/ocean_generic_tracer.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/mixing/ocean_bihgen_friction.F90 $(SRCROOT)shared/exchange/xgrid.F90                                            \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/internal_wave.F90 $(SRCROOT)atmos_param/sea_esf_rad/lhsw_driver.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/ice_sis/ice_thm.F90                                               \
/home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/cmue_a.F90 /home/wenchang/scratch/tiger3/MOM4.1/src/mom4p1/ocean_param/gotm-4.0/turbulence/potentialml.F90 $(SRCROOT)atmos_fv_dynamics/model/tp_core.F90
clean: neat
	-rm -f .fms_CM2.1p1_dynamic.x.cppdefs $(OBJ) fms_CM2.1p1_dynamic.x
neat:
	-rm -f $(TMPFILES)
localize: $(OFF)
	cp $(OFF) .
TAGS: $(SRC)
	etags $(SRC)
tags: $(SRC)
	ctags $(SRC)
fms_CM2.1p1_dynamic.x: $(OBJ) 
	$(LD) $(OBJ) -o fms_CM2.1p1_dynamic.x  $(LDFLAGS)
