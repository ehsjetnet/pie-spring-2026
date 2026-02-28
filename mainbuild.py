_HELPER_module_export_dict = {}
_HELPER_entry_point_line_nums = []
class _HELPER_Module:
    def __init__(self, module_name):
        self.__dict__ = _HELPER_module_export_dict[module_name]
    def __getitem__(self, key):
        return self.__dict__[key]
    def __setitem__(self, key, value):
        self.__dict__[key] = value
def _HELPER_entry_point(func):
    import functools
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print('Source traceback (most recent call last):')
            frame_lines = []
            tb = e.__traceback__
            while tb:
                translation_result = _HELPER_translate_line_no(tb.tb_lineno)
                if not translation_result:
                    tb = tb.tb_next
                    continue
                module_path, line_no = translation_result
                frame_lines.append(f'  File "{module_path}", line {line_no}, in {tb.tb_frame.f_code.co_name}')
                tb = tb.tb_next
            print('\n'.join(frame_lines))
            print(type(e).__name__ + (': ' if str(e) else '') + str(e))
            exit(1)
    return wrapped
def _HELPER_translate_line_no(line_no):
    if line_no >= 42:
        skipped_lines = 0
        for entry_point_line_num in _HELPER_entry_point_line_nums:
            if entry_point_line_num + 42 <= line_no:
                skipped_lines += 1
            else:
                break
        return 'main', line_no - 42 - skipped_lines
# End imports.

