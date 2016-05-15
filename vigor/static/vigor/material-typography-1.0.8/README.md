# Material Typography

Typography based on Google's Material Design Standard; available in CSS, LESS, SASS, SCSS, and Stylus.

[![Build Status](https://travis-ci.org/juliancoleman/material-typography.svg?branch=master)](https://travis-ci.org/juliancoleman/material-typography)

### Install Instructions

#### NPM

```
npm install --save material-typography
```

#### Bower

```
bower install material-typography
```

Or simply download the `.zip` and place it in your project folder wherever you'd like, then include your flavor of `typography` in your primary stylesheet.

For example:

```css
@import "material-typography/css/typography.min.css";
```

Or

```html
<link rel="stylesheet" href="node_modules/material-typography/css/typography.min.css" />
```

# Typography

## Typeface

#### Roboto

Roboto has been refined extensively to work across the wider set of supported platforms. It is slightly wider and rounder, giving it greater clarity and making it more optimistic.

![Examples of Roboto](https://material-design.storage.googleapis.com/publish/material_v_4/material_ext_publish/0Bx4BSt6jniD7SW9CUzR4MnRpOTg/style_typography_roboto1.png)

![Roboto A-Z and numerals](https://material-design.storage.googleapis.com/publish/material_v_4/material_ext_publish/0Bx4BSt6jniD7Y3JIMkV5ZmVaM2c/style_typography_roboto2.png)

#### Roboto font weights

Roboto has six weights: Thin, Light, Regular, Medium, Bold, and Black.

![Roboto font weights](https://material-design.storage.googleapis.com/publish/material_v_4/material_ext_publish/0Bx4BSt6jniD7ZHlGSHpsMjU5YmM/style_typography_weights1.png)

#### Font stack

```css
'Roboto', 'Noto', sans-serif;
```

## Styles

Too many type sizes and styles at once can wreck any layout. A typographic scale has a limited set of type sizes that work well together along with the layout grid.

These sizes and styles were developed to balance content density and reading comfort under typical usage conditions. Type sizes are specified with sp (scaleable pixels) to enable large type modes for accessibility.

The basic set of styles are based on a typographic scale of 12, 14, 16, 20, and 34.

##### Across form factors, text that appears in the app bar should use the Title style, Medium 20sp

Button style (Medium 14sp, all caps) is used for all buttons. Button text should be all caps in languages that have capitalization. For languages that don’t have capitals, consider using color text for flat buttons to make them stand out from normal text.

## Line Height

To achieve proper readability and appropriate pacing, line heights have been determined based on each style’s individual size and weight. Line wrapping only applies to Body, Subhead, Headline, and the smaller Display styles. All other styles should exist as single lines.

#### English and English-like scripts

![](https://material-design.storage.googleapis.com/publish/material_v_4/material_ext_publish/0Bzhp5Z4wHba3Q1VaNVBsdFozUTg/style_typography_styles_lineheight1.png)

![](https://material-design.storage.googleapis.com/publish/material_v_4/material_ext_publish/0Bzhp5Z4wHba3S0hlSFBQRVE0QlU/style_typography_styles_lineheight2.png)

![](https://material-design.storage.googleapis.com/publish/material_v_4/material_ext_publish/0B6Okdz75tqQsSDJtU2ZnVDZhTGM/style_typography_styles_lineheight3.png)
