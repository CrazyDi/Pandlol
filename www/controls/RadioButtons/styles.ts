import { createUseStyles } from 'react-jss'

export interface StyleProps {
}

export default createUseStyles({
    component: (props: StyleProps) => ({
        display: 'inline-flex'
    })
})
