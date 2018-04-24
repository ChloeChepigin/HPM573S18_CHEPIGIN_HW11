import ParameterClasses as P
import MarkovModel as MarkovCls
import SupportMarkovModel as SupportMarkov
import scr.SamplePathClasses as PathCls
import scr.FigureSupport as Figs

# create cohort for no treatment
cohortnotreatment = MarkovCls.Cohort(
    id=0,
    therapy=P.Therapies.NONE
)
simOutputs_Notreatment = cohortnotreatment.simulate()

# create a cohort for the anticoagulant
cohortanticoag = MarkovCls.Cohort(
    id=3,
    therapy=P.Therapies.ANTICOAG
)
simOutputs_Anticoag = cohortanticoag.simulate()


# report the CEA results
SupportMarkov.report_CEA_CBA(simOutputs_Anticoag, simOutputs_Notreatment)