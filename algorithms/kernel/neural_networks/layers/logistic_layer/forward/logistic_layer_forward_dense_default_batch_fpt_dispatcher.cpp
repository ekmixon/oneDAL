/* file: logistic_layer_forward_dense_default_batch_fpt_dispatcher.cpp */
/*******************************************************************************
* Copyright 2014-2020 Intel Corporation
*
* Licensed under the Apache License, Version 2.0 (the "License");
* you may not use this file except in compliance with the License.
* You may obtain a copy of the License at
*
*     http://www.apache.org/licenses/LICENSE-2.0
*
* Unless required by applicable law or agreed to in writing, software
* distributed under the License is distributed on an "AS IS" BASIS,
* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
* See the License for the specific language governing permissions and
* limitations under the License.
*******************************************************************************/

//++
//  Implementation of logistic function calculation algorithm container.
//--

#include "algorithms/kernel/neural_networks/layers/logistic_layer/forward/logistic_layer_forward_batch_container.h"

namespace daal
{
namespace algorithms
{
namespace neural_networks
{
namespace layers
{
namespace forward
{
__DAAL_INSTANTIATE_DISPATCH_LAYER_CONTAINER_FORWARD(neural_networks::layers::logistic::forward::BatchContainer, DAAL_FPTYPE,
                                                    neural_networks::layers::logistic::defaultDense)
}
} // namespace layers
} // namespace neural_networks
} // namespace algorithms
} // namespace daal