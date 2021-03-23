from config.graph_definition import compatibility_graph
from LicenseCompatibilityMatrix import LicenseCompatibilityMatrix

dp = LicenseCompatibilityMatrix(compatibility_graph)
print(dp.applicable_licenses(['AFL-3.0', 'MIT']))
print(dp.is_compatible('MIT', 'AFL-3.0'))