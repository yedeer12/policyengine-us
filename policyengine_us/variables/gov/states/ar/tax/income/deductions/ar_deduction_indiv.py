from policyengine_us.model_api import *


class ar_deduction_indiv(Variable):
    value_type = float
    entity = Person
    label = "Arkansas deduction when married couples are filing separately"
    unit = USD
    definition_period = YEAR
    reference = "https://www.dfa.arkansas.gov/images/uploads/incomeTaxOffice/2022_AR1000F_and_AR1000NR_Instructions.pdf#page=14"
    defined_for = "ar_can_file_separate_on_same_return"

    def formula(person, period, parameters):
        itemized = person("ar_itemized_deductions_indiv", period)
        standard = person("ar_standard_deduction_indiv", period)
        return max_(itemized, standard)
