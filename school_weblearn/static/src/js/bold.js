odoo.define('mypet.bold', function (require) {
    "use strict";
    // import packages
    var basic_fields = require('web.basic_fields');
    var registry = require('web.field_registry');

    //widget implementation
    var BoldWidget = basic_fields.FieldChar.extend({
        _renderReadonly: function() {
            this._super();
            var old_render_html = this.$el.html();
            var new_render_html = '<b style="color:red">' + old_render_html + '</b>';
            this.$el.html(new_render_html);
        }
    })
    registry.add('bold_red', BoldWidget)
})