from yattag import Doc, indent
from .SimpleContent import *
from ..common import WQXException

class CollectionEffort:
  """The fields to describe the effort used a collection."""

  __measureValue: MeasureValue
  __gearProcedureUnitCode: GearProcedureUnitCode

  def __init__(self, o=None, *,
    measureValue:MeasureValue = None,
    gearProcedureUnitCode:GearProcedureUnitCode = None
  ):
    if isinstance(o, CollectionEffort):
      # Assign attributes from object without typechecking
      self.__measureValue = o.measureValue
      self.__gearProcedureUnitCode = o.gearProcedureUnitCode
    elif isinstance(o, dict):
      # Assign attributes from dictionary with typechecking
      self.measureValue = o.get('measureValue', default = None)
      self.gearProcedureUnitCode = o.get('gearProcedureUnitCode', default = None)
    else:
      # Assign attributes from named keywords with typechecking
      self.measureValue = measureValue
      self.gearProcedureUnitCode = gearProcedureUnitCode

  @property
  def measureValue(self) -> MeasureValue:
    return self.__measureValue
  @measureValue.setter
  def measureValue(self, val:MeasureValue) -> None:
    self.__measureValue = MeasureValue(val)

  @property
  def gearProcedureUnitCode(self) -> GearProcedureUnitCode:
    return self.__gearProcedureUnitCode
  @gearProcedureUnitCode.setter
  def gearProcedureUnitCode(self, val:GearProcedureUnitCode) -> None:
    self.__gearProcedureUnitCode = GearProcedureUnitCode(val)

  def generateXML(self):
    if self.__measureValue is None:
      WQXException("Attribute 'measureValue' is required.")
    if self.__gearProcedureUnitCode is None:
      WQXException("Attribute 'gearProcedureUnitCode' is required.")

    doc, tag, text, line = Doc().ttl()

    line('MeasureValue', self.__measureValue)
    line('GearProcedureUnitCode', self.__gearProcedureUnitCode)

    return doc.getvalue()
