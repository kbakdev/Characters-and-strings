struct _zval_struct {
    /* Variable information */
    zvalue_value value;         /* value */
    zend_uint refcount__gc;
    zend_uchar type; /* active type */
    zend_uchar is_ref__gc;
};