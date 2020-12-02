from enum import IntEnum

class UponCompletionCondition( IntEnum ):

  NOT_APPLICABLE = 0
  EXPORT_IF_NO_ERROR = 1
  EXPORT_IF_NO_WARNING = 2
  EXPORT_ALWAYS = 3
