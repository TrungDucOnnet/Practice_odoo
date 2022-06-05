odoo.define('color_picker.ColorPicker', function(require){
    const { Component } = owl;

    const AbstractField = require('web.AbstractFieldOwl');
    const FieldRegistry = require('web.field_registry_owl');

    class ColorPillDemo extends Component {
        static template = 'ColorPillDemo';

        color_selected(){
            this.trigger('color-update', {val: this.props.color_no})
        }
    }

    class ColorPickerDemo extends AbstractField {
        static template = 'ColorPickerDemo';
        static components = {
            ColorPillDemo,
        }
        static supportedFieldTypes = ['integer'];

        constructor(...args) {
            super(...args);
            this.total_colors = Array.from({length: 10}, (_, i) => (i+1).toString())
        }

        color_update(ev){
            this._setValue(ev.detail.val)
        }
    }

    FieldRegistry.add('Color Picker Field', ColorPickerDemo);
})