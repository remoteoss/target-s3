from simplejson import dumps

from target_s3.formats.format_base import FormatBase, default_json_serializer


class FormatJson(FormatBase):
    def __init__(self, config, context) -> None:
        super().__init__(config, context, "json")
        pass

    def _prepare_records(self):
        # use default behavior, no additional prep needed
        # TODO: validate json records?
        return super()._prepare_records()

    def _write(self) -> None:
        return super()._write(
            dumps(
                self.records,
                default=default_json_serializer,
                use_decimal=True,
                ignore_nan=True,
            )
        )

    def run(self) -> None:
        # use default behavior, no additional run steps needed
        return super().run(self.context["records"])
