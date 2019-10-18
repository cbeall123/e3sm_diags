# Running the software with the API:
#    python all_sets_api.py -d all_sets.py
from acme_diags.parameter.core_parameter import CoreParameter
from acme_diags.parameter.zonal_mean_2d_parameter import ZonalMean2dParameter
from acme_diags.parameter.meridional_mean_2d_parameter import MeridionalMean2dParameter
from acme_diags.parameter.area_mean_time_series_parameter import AreaMeanTimeSeriesParameter
from acme_diags.parameter.enso_diags_parameter import EnsoDiagsParameter
from acme_diags.run import Run
import numpy

thing = Run()
param = CoreParameter()
ts_param = AreaMeanTimeSeriesParameter()

z2d_param = ZonalMean2dParameter()
z2d_param.plevs = [200., 300.,]
m2d_param = MeridionalMean2dParameter()
m2d_param.plevs = [200., 500.,]

enso_param = EnsoDiagsParameter()
enso_param.test_name = 'e3sm_v1'
enso_param.start_yr = '2000'
enso_param.end_yr = '2004'

import os
machine_path_prefix = '/global/project/projectdirs/acme/acme_diags'
param.reference_data_path = os.path.join(machine_path_prefix, 'obs_for_e3sm_diags/time-series')
param.test_data_path = os.path.join(machine_path_prefix, 'test_model_data_for_acme_diags/time-series/E3SM_v1')

thing.run_diags([param, ts_param, z2d_param, m2d_param, enso_param])

