import { createUseStyles } from 'react-jss'

export default createUseStyles({
    '@font-face': [
        {
            fontFamily: 'Roboto-Regular',
            src: 'url(assets/fonts/Roboto-Regular.ttf)'
        },
        {
            fontFamily: 'Roboto-Medium',
            src: 'url(assets/fonts/Roboto-Medium.ttf)'
        }
    ],
    '@global': {
        html: {
            height: '100%',
            boxSizing: 'border-box'
        },
        '*, *: before, *: after': {
            boxSizing: 'inherit'
        },
        body: {
            height: '100%',
            margin: 0,
            padding: 0,
            backgroundColor: '#f7f7f7'
        },
        'html, button, input, textarea': {
            fontFamily: 'Roboto-Regular, sans-serif',
            fontSize: '16px'
        },
        textarea: {
            resize: 'none'
        }
    }
})
