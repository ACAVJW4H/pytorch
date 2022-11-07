# Owner(s): ["module: dynamo"]

from torch._dynamo.testing import make_test_cls_with_patches

try:
    from . import (
        test_export,
        test_functions,
        test_misc,
        test_modules,
        test_no_fake_tensors,
        test_repros,
        test_subgraphs,
        test_unspec,
    )
except ImportError:
    import test_export
    import test_functions
    import test_misc
    import test_modules
    import test_no_fake_tensors
    import test_repros
    import test_subgraphs
    import test_unspec

import unittest


def make_dynamic_cls(cls):
    return make_test_cls_with_patches(
        cls, "DynamicShapes", "_dynamic_shapes", ("dynamic_shapes", True)
    )


DynamicShapesFunctionTests = make_dynamic_cls(test_functions.FunctionTests)
DynamicShapesMiscTests = make_dynamic_cls(test_misc.MiscTests)
DynamicShapesReproTests = make_dynamic_cls(test_repros.ReproTests)
DynamicShapesNNModuleTests = make_dynamic_cls(test_modules.NNModuleTests)
DynamicShapesUnspecTests = make_dynamic_cls(test_unspec.UnspecTests)
DynamicShapesExportTests = make_dynamic_cls(test_export.ExportTests)
DynamicShapesSubGraphTests = make_dynamic_cls(test_subgraphs.SubGraphTests)


# DynamicShapesFunctionTests
unittest.expectedFailure(
    DynamicShapesFunctionTests.test_len_tensor_dynamic_shapes
    # TypeError: 'torch._C.SymIntNode' object cannot be interpreted as an integer
)

unittest.expectedFailure(
    DynamicShapesFunctionTests.test_tensor_len_dynamic_shapes
    # TypeError: 'torch._C.SymIntNode' object cannot be interpreted as an integer
)


unittest.expectedFailure(
    DynamicShapesReproTests.test_issue175_dynamic_shapes
    # TypeError: 'torch._C.SymIntNode' object cannot be interpreted as an integer
)

unittest.expectedFailure(
    DynamicShapesReproTests.test_do_paste_mask_dynamic_shapes
    # aten.min.dim - couldn't find symbolic meta function/decomposition
)

unittest.expectedFailure(
    DynamicShapesReproTests.test_convert_boxes_to_pooler_format_dynamic_shapes
    # Could not infer dtype of torch._C.SymIntNode
)

unittest.expectedFailure(
    DynamicShapesReproTests.test_hf_t5_forward_dynamic_shapes
    # Cannot call sizes() on tensor with symbolic sizes/strides
)

unittest.expectedFailure(
    DynamicShapesReproTests.test_guard_fail_tensor_bool_dynamic_shapes
    # RuntimeError: aten.allclose.default - couldn't find symbolic meta function/decomposition
)

# DynamicShapesExportTests
unittest.expectedFailure(
    DynamicShapesExportTests.test_export_with_constant_list_nonzero_dynamic_shapes
)
unittest.expectedFailure(
    DynamicShapesExportTests.test_export_with_constant_list_nonzero_free_function_dynamic_shapes
)
unittest.expectedFailure(
    DynamicShapesExportTests.test_export_with_constant_tuple_nonzero_dynamic_shapes
)
unittest.expectedFailure(
    DynamicShapesExportTests.test_export_with_constant_tuple_nonzero_dynamic_shapes
)


# DynamicShapesSubGraphTests
unittest.expectedFailure(
    DynamicShapesSubGraphTests.test_enumerate_not_break_graph_dynamic_shapes
)
unittest.expectedFailure(DynamicShapesSubGraphTests.test_restore_state_dynamic_shapes)


if __name__ == "__main__":
    from torch._dynamo.test_case import run_tests

    run_tests()
