import React from 'react'

import Label from 'app/controls/label'
import Link, { LinkType } from 'app/controls/link'
import Button from 'app/controls/button'
import Preloader from 'app/components/preloader'
import MasterPage from 'app/components/master-page'

interface Props {
}

const HomePage = (props: Props) => {
    return (
        <MasterPage>
            <Label>Home Page</Label>
            <br/>
            <Link to="/test1" disabled>Disabled Link</Link>
            <br/>
            <Link to="/test2">Internal Link</Link>
            <br/>
            <Link to="https://google.com" type={LinkType.External} target="_blank">External Link</Link>
            <br/>
            <Link to="/test3" type={LinkType.Navigation}>Navigation Link</Link>
            <br/>
            <Button disabled>Disabled Button</Button>
            <br/>
            <Button>Button</Button>
            <br/>
            <Preloader /><Label>Preloader Label</Label>
            <br/>
        </MasterPage>
    )
}

export default HomePage
