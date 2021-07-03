import { createUseStyles } from 'react-jss'
import BreakPoints, { BreakPoint } from 'app/common/breakpoints'

export default createUseStyles({
    root: {
        backgroundColor: '#f7f7f7',
        [BreakPoints.equalOrUp(BreakPoint.XS_480)]: {
            backgroundColor: '#f7f7f7'
        },
        [BreakPoints.equalOrDown(BreakPoint.LG_1200)]: {
            backgroundColor: '#f7f7f7'
        }
    },
    header: {
        backgroundColor: '#fff'
    },
    page: {
        padding: '12px'
    }
})
