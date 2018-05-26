import sys
sys.path.append('parser')
sys.path.append('eval')
#import mymodule

import parser_test
import eval_test


print(parser_test.run_tests())
print(eval_test.run_tests())