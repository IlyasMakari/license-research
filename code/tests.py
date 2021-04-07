from config.library_graph_definition import nodes, edges
from LicenseCompatibilityMatrix import LicenseCompatibilityMatrix

dp = LicenseCompatibilityMatrix(nodes, edges)

# Is the license of my software compatible with the license of my dependency?
print(dp.is_compatible(dependency_licence='MIT', derivative_license='Unlicense'))

# What license should I use if I have dependencies licensed under MIT, AFL and Apache?
print(dp.applicable_licenses(dependency_licenses=['MIT', 'AFL-3.0', 'Apache-2.0']))