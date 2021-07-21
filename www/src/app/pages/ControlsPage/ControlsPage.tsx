import React from 'react'
import Label from 'controls/Label'
import Link, { LinkType } from 'controls/Link'
import Button from 'controls/Button'
import CheckBox from 'controls/CheckBox'
import RadioButtons from 'controls/RadioButtons'
import RadioButton from 'controls/RadioButtons/RadioButton'
import DropDown from 'controls/DropDown'
import Preloader from 'app/components/preloader'
import MasterPage from 'app/components/MasterPage'

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

            <CheckBox>CheckBox</CheckBox>
            <br/>
            <CheckBox disabled>Disabled CheckBox</CheckBox>
            <br/>
            <CheckBox disabled checked>Disabled Checked CheckBox</CheckBox>
            <br/>

            <RadioButtons>
                <RadioButton value="1">RadioButton 1</RadioButton>
                <RadioButton value="2" disabled>Disabled RadioButton 2</RadioButton>
                <RadioButton value="3">RadioButton 3</RadioButton>
            </RadioButtons>
            <br/>
            <RadioButtons>
                <RadioButton value="1">RadioButton 1</RadioButton>
                <RadioButton value="2" disabled>Disabled RadioButton 2</RadioButton>
                <RadioButton value="3">RadioButton 3</RadioButton>
            </RadioButtons>
            <br/>

            <Preloader /><Label>Preloader Label</Label>
            <br/>
            <DropDown editable={true} items={[]} />
            <br/>
            <DropDown editable={true} items={[
                { value: '1', text: 'item 1' },
                { value: '2', text: 'item 2' },
                { value: '3', text: 'item 3', disabled: true },
                { value: '4', text: 'item 4' }
            ]} />
            <br/>
            <DropDown items={[]}/>
            <br/>
            <DropDown items={[
                {value: '1', text: 'item 1'},
                {value: '2', text: 'item 2'},
                {value: '3', text: 'item 3', disabled: true},
                {value: '4', text: 'item 4'}
            ]}/>
            <br/>
        </MasterPage>
    )
}

export default HomePage