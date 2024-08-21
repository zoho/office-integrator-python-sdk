try:
	from officeintegrator.src.com.zoho.officeintegrator.exception.sdk_exception import SDKException
	from officeintegrator.src.com.zoho.officeintegrator.util.constants import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class CombinePDFsParameters(object):
	def __init__(self):
		"""Creates an instance of CombinePDFsParameters"""

		self.__input_options = None
		self.__output_settings = None
		self.__key_modified = dict()

	def get_input_options(self):
		"""
		The method to get the input_options

		Returns:
			dict: An instance of dict
		"""

		return self.__input_options

	def set_input_options(self, input_options):
		"""
		The method to set the value to input_options

		Parameters:
			input_options (dict) : An instance of dict
		"""

		if input_options is not None and not isinstance(input_options, dict):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: input_options EXPECTED TYPE: dict', None, None)
		
		self.__input_options = input_options
		self.__key_modified['input_options'] = 1

	def get_output_settings(self):
		"""
		The method to get the output_settings

		Returns:
			CombinePDFsOutputSettings: An instance of CombinePDFsOutputSettings
		"""

		return self.__output_settings

	def set_output_settings(self, output_settings):
		"""
		The method to set the value to output_settings

		Parameters:
			output_settings (CombinePDFsOutputSettings) : An instance of CombinePDFsOutputSettings
		"""

		try:
			from officeintegrator.src.com.zoho.officeintegrator.v1.combine_pd_fs_output_settings import CombinePDFsOutputSettings
		except Exception:
			from .combine_pd_fs_output_settings import CombinePDFsOutputSettings

		if output_settings is not None and not isinstance(output_settings, CombinePDFsOutputSettings):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: output_settings EXPECTED TYPE: CombinePDFsOutputSettings', None, None)
		
		self.__output_settings = output_settings
		self.__key_modified['output_settings'] = 1

	def is_key_modified(self, key):
		"""
		The method to check if the user has modified the given key

		Parameters:
			key (string) : A string representing the key

		Returns:
			int: An int representing the modification
		"""

		if key is not None and not isinstance(key, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: key EXPECTED TYPE: str', None, None)
		
		if key in self.__key_modified:
			return self.__key_modified.get(key)
		
		return None

	def set_key_modified(self, key, modification):
		"""
		The method to mark the given key as modified

		Parameters:
			key (string) : A string representing the key
			modification (int) : An int representing the modification
		"""

		if key is not None and not isinstance(key, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: key EXPECTED TYPE: str', None, None)
		
		if modification is not None and not isinstance(modification, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: modification EXPECTED TYPE: int', None, None)
		
		self.__key_modified[key] = modification
