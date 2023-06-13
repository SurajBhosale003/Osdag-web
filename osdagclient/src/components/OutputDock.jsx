import React from 'react'
import { Input } from 'antd';

const OutputDock = ({ output }) => {
    return (
        <div>
            <h5>Output Dock</h5>
            <div className='subMainBody scroll-data'>
                {output ? Object.keys(output).map((key, index) => {
                    return (
                        <div key={index}>
                            <h3>{key}</h3>
                            <div className='component-grid'>
                                {Object.values(output[key]).map((elm, index1) => {
                                    return (
                                        <div key={index1}>
                                            <div>
                                                <h4>{elm.label}</h4>
                                            </div>
                                            <div>
                                                <Input
                                                    type="text"
                                                    name={`${key}_${elm.lable}`}
                                                    value={elm.val}
                                                    disabled
                                                />
                                            </div>
                                        </div>
                                    );
                                })}
                            </div>
                        </div>
                    );
                }) :
                    <div>
                        <h3>No data</h3>
                    </div>}
            </div>
        </div>
    )
}

export default OutputDock